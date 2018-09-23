import pygame
from random import randint

class Brick():

    def __init__(self,block_size):
        self.block_size=block_size
        rand=randint(0,0)
        if rand==0:
            # square
            self.point=[(0,0),(0,1),(1,0),(1,1)]

    def draw(self,x,y):
        pygame.draw.rect(pygame.display.get_surface(),(255,255,200),pygame.Rect(x,y,self.block_size,self.block_size))
