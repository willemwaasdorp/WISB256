import urllib.request
conn = urllib.request.urlopen('http://thinkpython.com/secret.html')
for line in conn.fp:
    print(line.strip())