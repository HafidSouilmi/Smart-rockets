from vecteur import *
import pygame
from params import *


def DNA():
    return[random2D(k) for i in range(lifespan)]

def croisement(parentA,parentB):
    A=parentA.DNA
    B=parentB.DNA
    enfant=robot()
    n=len(A)
    m=random.randrange(n)
    for i in range(n):
        if i<=m:
            enfant.DNA[i]=A[i]
        else:
            enfant.DNA[i]=B[i]
    return enfant


class robot:

    def __init__(self):
        self.pos=vecteur(w/2-20,h-80)
        self.vel=vecteur()
        self.acc=vecteur()
        self.img=pygame.image.load('C://Users//Ilias//TIPE//rocket.png')
        self.DNA=DNA()
        self.fitness=0
        self.succes=False
        self.collision=False
        self.traj=[]

    def appliquerforce(self,force):
        self.acc+=force

    def maj(self,count):
        if distance(self.pos,target)<=r:
            self.succes=True
        if self.pos.x>=x and self.pos.x<x+ow and self.pos.y>y and self.pos.y<y+oh or self.pos.x>w or self.pos.x<0 or self.pos.y>h or self.pos.y<0:
            self.collision=True
        if self.succes==False and self.collision==False:
            self.appliquerforce(self.DNA[count])
            self.vel+=self.acc
            self.pos+=self.vel
            self.acc*=0
            self.traj.append(self.pos)

    def show(self,win):
        win.blit(pygame.transform.rotate(self.img,270-orientation(self.vel)),(self.pos.x-20,self.pos.y-36))
        n=len(self.traj)
        for i in range(1,n-1,3):
            pygame.draw.line(win,(0,0,255),(self.traj[i].x,self.traj[i].y),(self.traj[i+1].x,self.traj[i+1].y))
    
    def mutation(self):
        n=len(self.DNA)
        for i in range(n):
            if random.uniform(0,1)<=pmut:
                self.DNA[i]=random2D(k)

