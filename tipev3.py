import pygame
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

class robot:
    def __init__(self):
        global target
        global r
        self.pos=vecteur(w/2-20,h-80)
        self.vel=vecteur()
        self.acc=vecteur()
        self.img=pygame.image.load('C://Users//ASUS ROG//Desktop//TIPE//rocket.png')
        self.DNA=DNA()
        self.fitness=0
        self.succes=False
        self.collision=False
        self.traj=[]
    def appliquerforce(self,force):
        self.acc+=force
    def maj(self):
        global count,target,r,x,y,ow,oh,succes
        if distance(self.pos,target)<=r:
            self.succes=True
            succes=True
        if self.pos.x>=x and self.pos.x<x+ow and self.pos.y>y and self.pos.y<y+oh or self.pos.x>w or self.pos.x<0 or self.pos.y>h or self.pos.y<0:
            self.collision=True
        if self.succes==False and self.collision==False:
            self.appliquerforce(self.DNA[count])
            self.vel+=self.acc
            self.pos+=self.vel
            self.acc*=0
            self.traj.append(self.pos)
    def show(self):
        win.blit(pygame.transform.rotate(self.img,270-orientation(self.vel)),(self.pos.x-20,self.pos.y-36))
        n=len(self.traj)
        for i in range(1,n-1,3):
            pygame.draw.line(win,(0,0,255),(self.traj[i].x,self.traj[i].y),(self.traj[i+1].x,self.traj[i+1].y))
    
        
        
    def mutation(self):
        global mutcount,pmut,k
        n=len(self.DNA)
        for i in range(n):
            if random.uniform(0,1)<=pmut:
                self.DNA[i]=random2D(k)
                
                
        
class population:
    def __init__(self,n):
        self.robots=[]
        self.popsize=n
        for i in range(self.popsize):
            self.robots.append(robot())
        self.matingpool=[]
    def selection(self):
        self.evaluer()
        self.matingpool.clear()
        for i in range(self.popsize):
            j=int(self.robots[i].fitness*100)
            for k in range(j):
                self.matingpool.append(self.robots[i])
    def reproduction(self):
        self.selection()
        newrobots=[]
        for i in range(self.popsize):
            parentA=random.choice(self.matingpool)
            parentB=random.choice(self.matingpool)
            enfant=croisement(parentA,parentB)
            enfant.mutation()
            newrobots.append(enfant)
        self.robots=newrobots
    def play(self):
        for r in self.robots:
            if succes==False:
                r.maj()
            r.show()
    def evaluer(self):
        global target,succes,h
        m=0
        for robot in self.robots:
            robot.fitness=(h/distance(target,robot.pos))**4
            if robot.collision==True:
                robot.fitness/=100
            if robot.succes==True:
                robot.fitness*=100
                succes=True
            if robot.fitness>m: m=robot.fitness
        print(m)
        for robot in self.robots:
            robot.fitness/=m
            
def orientation(vector):
    return np.angle(complex(vector.x,vector.y),deg=True)
    
def random2D(k):
    x=random.uniform(-1,1)
    y=(1-x**2)**(1/2)*((-1)**(random.randint(0,1)))
    return vecteur(x,y)*(1/(k**(1/2)))
    
def DNA():
    global lifespan,k
    return[random2D(k) for i in range(lifespan)]
    
def distance(u,v):
    return ((u.x-v.x)**2+(u.y-v.y)**2)**(1/2)

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


k=15
w=900
h=700
lifespan=600
count=0
r=25
target=vecteur(w//2,r)
pygame.init()
win=pygame.display.set_mode((w,h))
pygame.display.set_caption("TIPE")
pop=population(25)
pmut=0.01
gencount=0
x=225
y=400
ow=450
oh=50
succes=False
run=True
myfont = pygame.font.SysFont("arial", 20)
messageS=myfont.render("Succès !", 1, (0,255,0))
while run:
    win.fill((255,255,255))
    pygame.draw.circle(win, (0,255,0), (target.x,target.y),25)
    pygame.draw.rect(win,(255,0,0),(x,y,ow,oh))
    compteurcount = myfont.render('âge de la génération : '+str(count), 1, (255,0,0))
    win.blit(compteurcount, (20, 20))
    compteurgen = myfont.render('génération n° :'+str(gencount), 1, (255,0,0))
    win.blit(compteurgen, (20,40))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if succes==False:
        if count!=lifespan:
            pop.play()
            pygame.time.delay(10)
            pygame.display.update()
            count+=1
        else:
            pop.reproduction()
            count=0
            gencount+=1
    else:
        pop.play()
        win.blit(messageS,(20,60))
        count=lifespan-1
        pygame.display.update()
           
pygame.quit()

    
        
        
        
        
        
        