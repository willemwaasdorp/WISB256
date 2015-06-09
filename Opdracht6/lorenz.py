import numpy as np
from scipy.integrate import odeint 
import scipy 
class Lorenz:
    def __init__(self, invoer, sigma=10.0, rho=28.0 , beta = 8/3.0):
        self.initial = invoer
        self.x = invoer[0]
        self.y = invoer[1]
        self.z = invoer[2]
        self.x_dot = sigma * (self.y - self.x)
        self.y_dot = self.x * (rho - self.z) - self.y
        self.z_dot = self.x * self.y - beta * self.z
    def solve(self, t,dt):
        time = scipy.arange(0, t, dt)
        return odeint([self.x_dot,self.y_dot,self.z_dot], self.initial, time)