import math
class Vector:
     
     def __init__(self,n, invoer=0.0):
         self.vector = []
         for i in range(n):
             self.vector.append(invoer)
         self.length = n    
     def __str__(self):
         beeld = ""
         for i in range(self.length):
             beeld = beeld + str(self.vector[i]) + "\n"
         return beeld    
     def lincomb(self,other,alpha,beta):
         pass
     def scalar(self,alpha):
         b = self
         for i in range(self.length):
             b.vector[i] = b.vector[i] * alpha
         return b    
     def inner(self,other):
         pass
     def norm(self):
         pass
v = Vector(3,2.4) 
d = v.scalar(2)
print(v)