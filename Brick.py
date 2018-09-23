import pygame
from random import randint

class Brick():

    def __init__(self,board):
        self.board=board
        self.block_size=board.block_size
        rand=randint(0,1)
        if rand==0:
            # square
            self.point=[(0,0),(0,1),(1,0),(1,1)]
        elif rand==1:
            self.point=[(0,0),(1,0),(2,0),(3,0)]
        self.x=0
        self.y=0
        self.speed=1

    def draw(self):
        for point in self.point:
            pygame.draw.rect(pygame.display.get_surface(),(255,255,200),pygame.Rect(self.x+self.board.x+point[0]*self.block_size,self.y+self.board.y+point[1]*self.block_size,self.block_size,self.block_size))
        pygame.display.flip()

    def move_down(self):
        self.y+=self.speed

    def move_left(self):
        self.x-=self.speed

    def move_right(self):
        self.x+=self.speed
