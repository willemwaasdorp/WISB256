import re
import os
import urllib.request
from scipy.sparse import coo_matrix
import numpy as np
import scipy.sparse as sp
from numpy import linalg as LA

website = 'http://stratic-advice.nl'
site = 'http://www.'+ website.replace("http://","")
lijst_links = [website]

k=0
lijst_x_coordinaten = []
lijst_y_coordinaten = []
lijst_coordinaten = []
scorelijst = []


def webscraping(page,nummer):
    try:
        x = urllib.request.urlopen(page)        
    except (urllib.error.URLError, ValueError):
        return
    finalPage = []
    for line in x:
        if re.match("b' *[\<][na/!lsidu]", str(line),re.I) == None:
            finalPage.append(line)
    textfile = open('pages/'+ str(nummer) + '.text', 'wt')
    for regel in finalPage:
        textfile.write(str(regel) + '\n')
    return

def crawl(page,k):
    
    # probeer of url geopend kan worden
    try:
        x = urllib.request.urlopen(page)        
    except (urllib.error.URLError, ValueError):
        return
# plek 1 om te scrapen, dan wordt het proces alleen uitgevoerd voor pagina 0
    webscraping(page,k)
    
    for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
        #  maak bruikbare links
        
        if re.match('/', i) != None:
            i = i[1:]
        if re.match('http', i) == None:
                i = website + "/" + str(i)
        
        if (re.search(site, i) != None) or (re.search(website, i) != None):
                if i not in lijst_links:
                    # voeg link toe in lijst_links en zet coordinaat op 1
                    lijst_links.append(i)
                    lijst_coordinaten.append([k,len(lijst_links)-1])
                    
                else:
                    # voeg link niet toe, zet coordinaat op 1
                    index = lijst_links.index(i)
                    if index != k and [k,index] not in lijst_coordinaten: 
                        lijst_coordinaten.append([k,index])
    return


    
    
# lijst met links, elke link wordt gecrawld
for page in lijst_links:
    crawl(page,k)
    k += 1                                     
    
# maak 2 lijsten, 1 met x coordinaten en 1 met y coordinaten
for i in range(len(lijst_coordinaten)):
    lijst_x_coordinaten.append(lijst_coordinaten[i][0])
    lijst_y_coordinaten.append(lijst_coordinaten[i][1])

# maak data met 1'en en maak sparsematrix
data = [1] * len(lijst_x_coordinaten)
matrix = coo_matrix((data, (lijst_y_coordinaten, lijst_x_coordinaten))).toarray()


# voorbeeld van input
# rows= [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]
# cols= [1, 0, 2, 3, 0, 1, 3, 4, 1, 2, 5, 6, 0, 2, 5, 3, 4, 6, 3, 5]
# values= [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# normaliseer de matrix
def normaliseer(cols, values):
    lijst=[]
    for i in range (len(cols)):
        a=values[i]/cols.count(cols[i])
        lijst.append(a)
    return(lijst)


valuesnorm = normaliseer(lijst_x_coordinaten, data)


# maak sparse matrix genormaliseerd
sparsematrix = sp.coo_matrix( (valuesnorm, (lijst_y_coordinaten, lijst_x_coordinaten)) )


# A = (alfa * P + (1-alfa) * C))   met C is n*n matrix van enen en P de genormaliseerde matrix
    
def matrixKeerVector(A, n):
    grootte = A.shape    
    A = 0.85 * A    
    vector = np.ones(grootte[0])/grootte[0]
    B = (0.15/grootte[0])*np.ones(shape=(grootte[0], grootte[0]))
    for i in range(n):
        uit = A.dot(vector)
        uit2 = B.dot(vector)
        vector = uit + uit2
    return vector


PageRank = matrixKeerVector(sparsematrix,100)
# print(matrixKeerVector(sparsematrix, 100))

zoekwoord = input("Geef een zoekwoord op.  ")

def zoeken(zoekwoord):
    path = os.path.dirname(os.path.abspath(__file__)) + '/pages/'
    zoekaantal = []
    # folder  = sort_nicely(os.listdir(path))
    folder = os.listdir(path)
    for filename in folder:
        nummer = filename[:-5]
        aantal = 0
        file = open(path + filename, 'r')
        for line in file:
            for i in re.findall(' ' + str(zoekwoord) + ' ', str(line),re.I):
                aantal += 1
        zoekaantal.append([nummer,aantal])
    return zoekaantal    

zoeklijst = zoeken(zoekwoord)
for i in range(len(zoeklijst)):
    zoeklijst[i][1] = zoeklijst[i][1] * PageRank[int(zoeklijst[i][0])]
zoeklijst = sorted(zoeklijst, reverse=True)
resultaat = open('resultaat.text', 'wt')
for i in range(len(zoeklijst)):
    if zoeklijst[i][1] != 0:
        resultaat.write(lijst_links[int(zoeklijst[i][0])] + '\n')
    
  