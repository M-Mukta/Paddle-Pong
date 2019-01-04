# -*- coding: utf-8 -*-
import pygame

white=(255,255,255)
red=(255,0,0)
pygame.init()
screen_x=1000
screen_y=500
win=pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Paddle pong")
clock=pygame.time.Clock()

class paddle:
    speed=10
    height=167
    width=35
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pygame.draw.rect(win,white,(self.x,self.y,self.width,self.height))
    
    def get_pos(self):
        return [self.x,self.y,self.x+self.width,self.y+self.height]
   
    def show(self):
        pygame.draw.rect(win,white,(self.x,self.y,self.width,self.height))
    
    def move_up(self):
        if self.y>0:
            self.y=self.y-self.speed
        pygame.draw.rect(win,white,(self.x,self.y,self.width,self.height))

    def move_down(self):
        if (self.y+self.height)<screen_y:
            self.y=self.y+self.speed
        pygame.draw.rect(win,white,(self.x,self.y,self.width,self.height))
        
class pong:
    speed_x=2
    speed_y=2
    height=35
    width=35
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pygame.draw.rect(win,red,(self.x,self.y,self.width,self.height))
        
    def get_pos(self):
        return [self.x,self.y,self.x+self.width,self.y+self.height]
        
    def  move(self):
        
        if self.y>=465 or self.y<=0:
            self.x=self.x+self.speed_x
            self.speed_y*=-1
            #print("0:",self.speed_y)
            self.y=self.y+self.speed_y
            
        elif self.x>=965 or self.x<=0:
            self.speed_x*=-1
            #print("1:",self.speed_y)
            self.x=self.x+self.speed_x
            self.y=self.y+self.speed_y
        else:
            self.x=self.x+self.speed_x
            self.y=self.y+self.speed_y
            #print("2:",self.speed_y)
        pygame.draw.rect(win,red,(self.x,self.y,self.width,self.height))
        
         
    def show(self):
        pygame.draw.rect(win,red,(self.x,self.y,self.width,self.height))

def collision(p1,p2,pong_obj):
    pong1=pong_obj.get_pos()
    if (p1[0] < pong1[2]) and (pong1[0] < p1[2]) and (p1[1] < pong1[3]) and (pong1[1] < p1[3]):
        pong_obj.speed_x*=-1
        #pong_obj.speed_y*=-1
        pong_obj.move()
    if (p2[0] < pong1[2]) and (pong1[0] < p2[2]) and (p2[1] < pong1[3]) and (pong1[1] < p2[3]):
        pong_obj.speed_x*=-1
        #pong_obj.speed_y*=-1
        pong_obj.move()
    
        
  
def play():
    p1=paddle(0,150)
    p2=paddle(965,150)
    pong1=pong(500,250)
    pygame.display.update()
    cnt=0
    while True:
        clock.tick(100)
        win.fill((0,0,0))
        p1.show()
        p2.show()
        if cnt==0:
            pong1.show()
            
        pong1.move()
        p1.pos=p1.get_pos()
        p2.pos=p2.get_pos()
        collision(p1.pos,p2.pos,pong1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                break
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            p2.move_up()
        if keys[pygame.K_DOWN]:
            p2.move_down()
        if keys[pygame.K_w]:
            p1.move_up()
        if keys[pygame.K_s]:
            p1.move_down()
        
        pygame.display.update() 
        
        cnt=cnt+1

    
    
play()
pygame.time.delay(10000)
pygame.quit()
    