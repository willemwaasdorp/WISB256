import math
import time
def sieve(n):
    t1 = time.perf_counter()
    prime = open('prime.dat', 'w')
    lijst = []
    for i in range(n+1):
        lijst.append(True)
    for k in range(2,n):
        if lijst[k] == True:
            getal = k**2
            while getal <= n:
                lijst[getal] = False
                getal = getal + k
    result = 0
    for i in range(2,n):
        if lijst[i] == True:
            print(i)
            prime.write(str(i) + '\n')
            result += 1
    t2 = time.perf_counter()
    prime.close()
    print("Found "+ str(result) + " Prime numbers smaller than " + str(n) + " in " + str(t2-t1) +  " sec.") 
    
sieve(30)            
            
    