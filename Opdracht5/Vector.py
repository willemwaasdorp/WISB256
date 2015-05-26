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
        b = Vector(self.length)
        for i in range(self.length):
            b.vector[i] = (alpha * self.vector[i]) + (beta * other.vector[i])
        return b
    def scalar(self,alpha):
        b = Vector(self.length)
        for i in range(self.length):
            b.vector[i] = self.vector[i] * alpha
        return b    
    def inner(self,other):
        pass
    def norm(self):
        pass
v = Vector(3,2) 
d = v.scalar(2)
print(v)
print(d)
w = v.lincomb(d,2,2)
print(w)