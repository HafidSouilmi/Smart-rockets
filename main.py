from vecteur import *
import params
from population import *
from robot import *
import pygame


pygame.init()
win=pygame.display.set_mode((w,h))
pygame.display.set_caption("SMART ROCKETS")
pop=population(params.n)
myfont = pygame.font.SysFont("arial", 20)
messageS=myfont.render("Succès !", 1, (0,255,0))
run=True
count=0
i=0

while run==True:
    
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
    if pop.succes==False:
        if count!=lifespan:
            pop.play(win,count)
            pygame.time.delay(1)
            pygame.display.update()
            count+=1
        else:
            pop.reproduction()
            count=0
            gencount+=1
    else:
        pop.play(win,count)
        win.blit(messageS,(20,60))
        count=lifespan-1
        pygame.display.update()
           
pygame.quit()