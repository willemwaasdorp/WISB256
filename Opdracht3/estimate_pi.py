import sys
import random
import math
try:
    L = sys.argv[2]
    n = sys.argv[1]
except IndexError:
    print("Use: estimate_pi.py N L")
    exit()
try:
    s = sys.argv[3]
except IndexError:
    s = ""

L = float(L)
n = int(n)
if L > 1:
    print("AssertionError: L should be smaller than 1")
    exit()
else:
    if s != "":
        random.seed(s)
    def drop_needle(L):
        x = random.random()
                
        a = random.vonmisesvariate(0,0)
        xn = x + L*math.cos(a)
        if a < 0.5 * math.pi or a > 1.5 * math.pi:
            if xn > math.ceil(x):
                return True
            else:
                return False
        elif a > 0.5 * math.pi or a < 1.5 * math.pi: 
            if xn < math.floor(x):
                return True
            else:
                return False

    counter = 0
    for i in range(n):
        if drop_needle(L) == True:
            counter += 1
        
    pi = (2 * L)/(counter/n)

    print(str(counter) + " hits in " + str(n) + " tries")
    print("Pi = " + str(pi))
    
