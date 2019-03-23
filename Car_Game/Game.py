"""
Created on Sat Mar  9 13:58:26 2019

@author: hussainsalih

"""

import pygame as p
import random as r
import time

# width and height of window
width = 400
height = 700

## enemy_images
enemy_img = [p.image.load("enemy_1.png"),p.image.load("enemy_2.png"),p.image.load("enemy_3.png"),p.image.load("enemy_4.png")]

#image of player
img = p.image.load("carplayer.png")

#background of game
bg = p.image.load("background.png")

p.init()

#for font 
p.font.init()

myfont = p.font.SysFont('Comic Sans MS', 80)

textsurface = myfont.render('', False, (255,255,255))

window = p.display.set_mode((width,height))

# name of window
p.display.set_caption("Car Game")

class Car():
    def __init__(self,src,x,y,f):
        self.src = src
        self.x = x
        self.y = y
        self.f = f

    def draw(self):
        window.blit(self.src,(self.x,self.y))
        
    def forward(self):
        self.y += self.f
        
    def move(self,spd):
        self.x -= spd
        if self.x < 30 :
            self.x = 30
        if self.x > 300:
            self.x = 300
        
    def collision(self,other):
        if(self.x < other.x + 70 and self.x + 70 > other.x and self.y + 140 > other.y and self.y < other.y + 140):
            return True
        else:
            return False
       
speed = 5

c = Car(img,100,560,0)

e = []

e.append(Car(enemy_img[r.randint(0,3)],r.randint(30,100),0,r.randint(1,2)))
e.append(Car(enemy_img[r.randint(0,3)],r.randint(180,300),0,r.randint(1,3)))

#player width = 80
#player height = 140


gameExit = False

while not gameExit:
        for event in p.event.get():
            if event.type==p.QUIT:
                gameExit = True
                gameOver = False
                p.quit()
                quit()
                    
        keys = p.key.get_pressed()
        
        if keys[p.K_LEFT]:
            c.move(speed)
        if keys[p.K_RIGHT]:
            c.move(-speed)
                
        window.blit(bg,(0,0))
        c.draw()
        
        for i in range(0,len(e)):
            e[i].forward()
            e[i].draw()
            if(e[i].collision(c)):
               textsurface = myfont.render('Game Over', False, (255,255,255))
               gameExit = True
               #quit()
               
        for i in range(0,len(e)):
            if(e[i].y > 800):
                del e[i]  
                p.mixer.music.load("move.mp3")
                p.mixer.music.play(0)
                e.append(Car(enemy_img[r.randint(0,3)],r.randint(30,300),0,r.randint(2,4)))
                     
        window.blit(textsurface,(50,330))
        
        p.display.update()
        
p.quit()
