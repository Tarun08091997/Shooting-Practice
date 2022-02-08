##This file contain all the sprites involved in game like aim, Target etc
import pygame
from Database import *
import random
pygame.init()


class aim_cursor(pygame.sprite.Sprite):
    list = []
    def __init__(self,aim_type=0):
        super().__init__()
        self.image = con.cursor_List[aim_type]
        self.rect = self.image.get_rect()
    def update(self,pos_x,pos_y):
        self.rect.center = (pos_x,pos_y)


    def shoot(self,group):
        
        con.gun_sound.play()
        self.list = pygame.sprite.spritecollide(self,group,True)

    def is_collision(self):
        if len(self.list)==0:
            return False
        else:
            return True



class Target(pygame.sprite.Sprite):

    def __init__(self,image):
       super().__init__()

       self.posx = random.randint(55, 1300)
       self.posy = random.randint(80, 700)

       self.image = image
       self.rect = self.image.get_rect()
       self.rect.center = (self.posx, self.posy)

    def show(self):
        self.rect.center = (self.posx,self.posy)


