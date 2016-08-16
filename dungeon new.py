import pygame
import dpylib
import math,random
from pygame import *
from os import mkdir
DISPLAY = (800, 640)
DEPTH = 16
FLAGS = pygame.RESIZABLE



screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
pygame.init()
display.set_caption("DungeonPy")
timer = time.Clock()

ent = pygame.sprite.Group()

#Connect Player and World
hud = Surface((800,128))

w=dpylib.World(ent,screen,hud)
p=dpylib.Player(384,224,w)
w.player=p
w.levelname="level"
def main():
    try:
        dpylib.loadlvl(ent,w.levelname+"\\world00.txt")
    except:

        #try to grab/create the level folder
        try:
            mkdir(w.levelname)
        except:
            pass
        
        dpylib.fill(ent)
        dpylib.carve(ent)
        dpylib.doors(ent)
        dpylib.savelvl(ent,w.levelname+"\\world"+str(w.pos[0])+str(w.pos[1])+".txt")
    go=True
    w.Draw()
    while go:
        mse=pygame.mouse.get_pos()
        mse=(((mse[0])/32)*32,((mse[1])/32)*32)
        dt=timer.tick(60)
        #speed = 1 / float(dt)
        #speed = 5 * speed
        #screen.fill((0,0,0))

        for e in pygame.event.get():
            if e.type == QUIT:
                if w.state=="game":
                    dpylib.savelvl(ent,w.levelname+"\\world"+str(w.pos[0])+str(w.pos[1])+".txt")
                go = False
                
        w.Update()
        
     
        pygame.display.flip()
        display.set_caption("DungeonPy - "+str(mse))
    pygame.display.quit()
    


if(__name__ == "__main__"):
    main()
