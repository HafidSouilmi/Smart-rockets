from params import *
from robot import *

class population:

    def __init__(self,n):
        self.robots=[]
        self.popsize=n
        for i in range(self.popsize):
            self.robots.append(robot())
        self.matingpool=[]
        self.succes=False

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

    def play(self,win,count):
        for r in self.robots:
            if self.succes==False:
                r.maj(count)
                if r.succes==True: 
                    self.succes=True
            r.show(win)

    def evaluer(self):
        m=0
        for robot in self.robots:
            robot.fitness=(h/distance(target,robot.pos))**4
            if robot.collision==True:
                robot.fitness/=100
            if robot.succes==True:
                robot.fitness*=100
            if robot.fitness>m: m=robot.fitness
        for robot in self.robots:
            robot.fitness/=m