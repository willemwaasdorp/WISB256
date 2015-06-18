import numpy as np
from scipy.integrate import odeint 
import scipy 
class Lorenz:
    def __init__(self, invoer, sigma=10.0, rho=28.0 , beta = 8/3.0):
        self.initial = invoer
        
        self.x_dot = sigma * (y - x)
        self.y_dot = x * (rho - z) - y
        self.z_dot = x * y - beta * z
    def solve(self, t,dt):
        time = scipy.arange(0, t, dt)
        return odeint([self.x_dot,self.y_dot,self.z_dot], self.initial, time)