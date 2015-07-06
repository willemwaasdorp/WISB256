import re
import urllib.request

textfile = open('depth_1.txt','wt')

website = 'http://www.stratic-advice.nl'
domain = 'www.'+ website.replace("http://","")
x = urllib.request.urlopen(website)
for t in re.findall('<h3>.+</h3>',str(x.read()), re.I):
        print(t)
        

        
