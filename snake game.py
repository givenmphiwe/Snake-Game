import math
import random
import pygame
import time
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500

    def _init_(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny) 
    
    def draw(self,surface,eyes=False):
        #figuring out the x and y values are in the screen
        dis = self.w // self.rows

        i = self.pos[0]
        j = self.pos[1]
        
        #to see the grid when drawing the rectangle or snake..like snake inside the square
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
         
        #the following are the eyes of the snake 
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body =[]
    turns = {}
    def _init_(self, color, pos):
        self.color = color
        self.head = cube(pos) 
        self.body.append(self.head)
        #dir to keep track of direction we are moving at 
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        #for moving the snake here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            #is gonna get a list of all key values if they were pressed or not
            keys = pygame.key.get_pressed()
            
            #looping through the all the keys to check if they were pressed
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    #this is for to remember where the snake turned so that the tail can follow
                    self.turns[seld.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    #this is for to remember where the snake turned so that the tail can follow
                    self.turns[seld.head.pos[:]] = [self.dirnx, self.dirny]
                    

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    #this is for to remember where the snake turned so that the tail can follow
                    self.turns[seld.head.pos[:]] = [self.dirnx, self.dirny]
                    

                elif keys[pygame.K_DOWN]: 
                    self.dirnx = 0
                    self.dirny = 1
                    #this is for to remember where the snake turned so that the tail can follow
                    self.turns[seld.head.pos[:]] = [self.dirnx, self.dirny]
            
            #moving our cube
            #for each object am gonna grab the position and am see the positionis in our turn list 
            for i, c in enumerate(self.body):
                p=c.pos[:] 
                if p in self.turns: 
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(self.body)-1: #if we are in the last cube we ganna remove that turn
                        self.turns.pop(p)              
                
                #we checking whether or not we have reached the edge of the screen
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c,pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                    #if we are not turning left or right..keep moving straight
                    else: c.move(c.dirnx,c.dirny)


    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        #adding snack 
        tail = self.body[-1]
        dx, dy = tai.dirnx, tail.dirny

        #to know where to add the cube/snack in the right position of where we are going 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1]))) 
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))            
        
        #where our tail is currently moving at the moment
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy



    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)    
    

def drawGrid(w, rows, surface):
    #how big the square needs to be in this function
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x=x + sizeBtwn
        y=y + sizeBtwn

        #drawing the lines in the x  and y axis
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()
    

def randomSnack(rows,  item):
    position = item.body
    
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        #to make sure we dont put a snack behind a snake or on the tail
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)

def message_box(subject, content):

    root.tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s,snack
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))
    Snack = cube(randomSnack(rows, s), color=(0,255,0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10) #snake will move 10 block in like one sec..i dont want to fast why i delayed it
        s.move()
        
        #check if the snake has hit head then add body
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))
        
        #checking if the position is in the list of all positions
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('score: ', len(s.body))
                message_box('you lost', 'Try again')
                s.reset((10,10))    
        redrawWindow(win)
    pass


main()

     
