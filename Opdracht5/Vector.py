from array import array
import math
class Vector:
     
    def __init__(self,n, invoer=0.0):
        self.vector = []
        if type(invoer) is int or type(invoer) is float:
            for i in range(n):
                self.vector.append(invoer)
            self.length = n 
        if type(invoer) is list or type(invoer) is array:
            for i in range(n):
                self.vector.append(invoer[i])
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
        antwoord = 0
        for i in range(self.length):
            antwoord += self.vector[i] * other.vector[i]
        return antwoord    
    def norm(self):
        return math.sqrt(self.inner(self))
        
