class Vectors:
     def __init__(self,n):
         self = []
         for i in range(n-1):
             print(i)
             self.append(0.000000)
     def __str__(self):
         for i in range(len(self)):
             print(self[i])
     def lincomb(self,other,alpha,beta):
        pass
     def scalar(self,alhpa):
         pass
     def inner(self,other):
         pass
     def norm(self):
         pass
v = Vectors(3) 
print(v)