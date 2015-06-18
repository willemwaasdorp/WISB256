import re
import urllib.request

textfile = open('depth_1.txt','wt')
# print("Enter the URL you wish to crawl..")
# print('Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes')
#myurl = input("@> ")
website = 'http://nu.nl'
x = urllib.request.urlopen(website)
for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
        # print(i) 
        if re.match('http', i) == None:
                i = website + str(i)
                #y = urllib.request.urlopen(website + str(i))
        if re.search('nu.nl', i) == None:
                next
        else:
                y = urllib.request.urlopen(i)
        for ee in re.findall('''href=["'](.[^"']+)["']''', str(y.read()), re.I):
                print(ee)       
                textfile.write(ee+'\n')
        
        
        # try:
        #         
        # except ValueError:
        #         y = 'http://nu.nl' + str(i)
        #         print(y)
        
#               
# textfile.close()