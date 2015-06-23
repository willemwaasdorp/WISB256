import re
import urllib.request

textfile = open('depth_1.txt','wt')

website = 'http://nu.nl'
domain = 'www.'+ website.replace("http://","")
x = urllib.request.urlopen(website)
for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
        
        if re.match('http', i) == None:
                i = website + str(i)
        
        if (re.search(domain, i) != None) or (re.search(website, i) != None):
                textfile.write(i+'\n')
                 
        else:        
                
                try:
                        y = urllib.request.urlopen(str(i))
                except urllib.error.URLError:
                        continue
                for ee in re.findall('''href=["'](.[^"']+)["']''', str(y.read()), re.I):
                      
                        
                                
                        if re.match('http', ee) == None:
                                ee = i + str(ee)
                                
                             
                        if (re.search(domain, ee) != None) or (re.search(website, ee) != None):
                                textfile.write(ee+'\n')
                             
        
        
