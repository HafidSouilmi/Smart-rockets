import random 
import tkinter as tk
from tkinter import *
import numpy as np

genepool=[(0,1),(1,0),(0,-1),(-1,0)]
labyrinthe= [[1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,1],
             [1,1,1,1,1,0,0,1,0,1],
             [1,0,0,0,0,0,0,1,0,1],
             [1,0,1,1,1,1,0,1,0,1],
             [1,0,1,0,0,0,0,1,0,1],
             [1,0,1,0,0,0,0,1,0,1],
             [1,1,1,0,0,1,1,1,1,1],
             [0,0,0,0,0,0,0,0,0,1],
             [0,1,1,1,1,1,1,1,1,1]]
#labyrinthe=10*[10*[0]]


a=1
b=8
population=[]
matingpool=[]
pmut=.15
n=len(labyrinthe)
N=int(input('population initiale:'))

fenetre=Tk()
w=720
grille=Canvas(fenetre,width=w,height=w,bg='white')
grille.pack()
for i in range(0,w,720//n):
    grille.create_line((i,0),(i,w))
    grille.create_line((0,i),(w,i))
for i in range(n):
    for j in range(n):
        if labyrinthe[i][j]==1:
            grille.create_rectangle((720//n)*j,(720//n)*i,(720//n)*(j+1),(720//n)*(i+1),fill='black')
            

        
def parcours(l):
    global a,b,n,labyrinthe
    position=[0,0]
    c=0
    for direction in l:
        x,y=position
        u,v=direction[0],direction[1]
        if 0<=x+u<=n-1 and 0<=y+v<=n-1 and labyrinthe[n-1-(y+v)][x+u]!=1 and (x,y)!=(a,b):
            position[0]+=direction[0]
            position[1]+=direction[1]
            c+=1
        else: break
    return position,c
        
def fitness(liste):
    global a,b
    x,y=parcours(liste)[0]
    c=parcours(liste)[1]
    l=len(liste)
    return(1/(abs(x-a)+abs(y-b)+1))
    
class chemin:
    def __init__(self,l):
        self.gene=l
        self.fitness=fitness(l)
def mutation(self,pmut):
    l=self.gene
    if random.randrange(100)<int(100*pmut):
        l[random.randrange(len(l))]=random.choice(genepool)
    return(chemin(l))
        
        
def genererchemin(n):
    liste=[random.choice(genepool)]
    while len(liste)<n:
        d=random.choice(genepool)
        if (d[0]+liste[-1][0],d[1]+liste[-1][1])!=(0,0): liste.append(d)
    return chemin(liste)
    
def initialiser(population,N,n):
    for i in range(N):
        population.append(genererchemin(n))
        
def selection(matingpool,fitmax):
    global population
    while len(matingpool)<2:
        for chemin in population:
            if (random.randrange(100)/100)<(chemin.fitness/fitmax):
                matingpool.append(chemin)
                
def croisement(c1,c2):
    n=len(c1.gene)
    m=random.randrange(n-1)
    return chemin(c1.gene[:m]+c2.gene[m:])
    
def meilleurchemin(liste):
    m=liste[0]
    for chemin in liste:
        if chemin.fitness>m.fitness or ( chemin.fitness==1 and chemin.fitness==m.fitness and parcours(chemin.gene)[1]<parcours(m.gene)[1] ):
            m=chemin
    return m
    
def rectangle(i,j,col):
    global n,grille
    grille.create_rectangle((720//n)*i,(720//n)*(n-j-1),(720//n)*(i+1),(720//n)*(n-j),fill=col)
    
def tracerparcours(chemin,couleur):
    rectangle(0,0,couleur)
    position=[0,0]
    for direction in chemin.gene:
        if position[0]+direction[0] in range(0,n) and position[1]+direction[1] in range(0,n) and position!=[a,b] and labyrinthe[n-1-(position[1]+direction[1])][position[0]+direction[0]]!=1:
            position[0]+=direction[0]
            position[1]+=direction[1]
            rectangle(position[0],position[1],couleur)
        else: break
        
c=1
initialiser(population,N,2*n)
while meilleurchemin(population).fitness!=1:
    m=meilleurchemin(population)
    #tracerparcours(m,'red')
    P=len(population)
    selection(matingpool,m.fitness)
    M=len(matingpool)
    print('génération :',c,'pop',P,'mp',M)
    population.clear()
    while len(population)<N:
        population.append(mutation(croisement(random.choice(matingpool),random.choice(matingpool)),pmut))
    matingpool.clear()
    c+=1
print("le but a été atteint après", c ,"générations !")
tracerparcours(meilleurchemin(population),'green')


        
        
            
                
    
    