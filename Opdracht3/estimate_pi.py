import sys
import random
L = int(sys.argv[2])
n = int(sys.argv[1])

def drop_needle(L):
    x = random.random()
    y = random.random()
    a = random.vonmisesvariate(0,0)
    
    if hit:
        return True
    else:
        return False

counter = 0
for i in range(n):
    if drop_needle(L) == True:
        counter += 1
        
pi = (2 * L)/(counter/n)

print(counter + " hits in " + n + " tries")
print("Pi = " + pi)
    
