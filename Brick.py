import pygame
from random import randint

class Brick():

    def __init__(self,board):
        self.board=board
        self.block_size=board.block_size
        self.accelerated=False
        rand=randint(0,3)
        if rand==0:
            # square
            self.point=[(0,0),(0,1),(1,0),(1,1)]
        elif rand==1:
            # stick
            self.point=[(0,0),(1,0),(2,0),(3,0)]
        elif rand==2:
            # t
            self.point=[(1,0),(0,1),(1,1),(2,1)]
        elif rand==3:
            # left l
            self.point=[(1,0),(1,1),(0,2),(1,2)]
        elif rand==4:
            # right l
            self.point=[(0,0),(0,1),(0,2),(1,2)]
        elif rand==5:
            # left dog
            self.point=[(0,0),(1,0),(1,1),(1,2)]
        elif rand==6:
            # right dog
            self.point=[(1,0),(2,0),(1,1),(0,1)]


        self.x=0
        self.y=0
        self.speed=1

    def draw(self):
        for point in self.point:
            pygame.draw.rect(pygame.display.get_surface(),(255,255,200),pygame.Rect(self.x+self.board.x+point[0]*self.block_size,self.y+self.board.y+point[1]*self.block_size,self.block_size,self.block_size))
        pygame.display.flip()

    def move_down(self):
        if self.accelerated:
            self.y+=10*self.speed
        else:
            self.y+=self.speed

    def move_left(self):
        self.x-=self.speed

    def move_right(self):
        self.x+=self.speed

    def accelerate(self):
        self.accelerated=True

    def stop_accelerate(self):
        self.accelerated=False
