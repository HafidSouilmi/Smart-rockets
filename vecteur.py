import random
import numpy as np


class vecteur:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,other):
        somme=vecteur(self.x+other.x,self.y+other.y)
        return somme
    def __sub__(self,other):
        diff=vecteur(self.x-other.x,self.y-other.y)
        return diff
    def __mul__(self,n):
        prod=vecteur(self.x*n,self.y*n)
        return prod


def random2D(k):
    x=random.uniform(-1,1)
    y=(1-x**2)**(1/2)*((-1)**(random.randint(0,1)))
    return vecteur(x,y)*(1/(k**(1/2)))


def distance(u,v):
    return ((u.x-v.x)**2+(u.y-v.y)**2)**(1/2)

def orientation(vector):
    return np.angle(complex(vector.x,vector.y),deg=True)