import numpy as np
from scipy.integrate import odeint 
class Lorenz:
    def __init__(self, invoer, sigma=10.0, rho=28.0 , beta = 8/3.0):
        self.x0 = invoer[0]
        self.y0 = invoer[1]
        self.z0 = invoer[2]
    def solve(self, t,dt):
        pass