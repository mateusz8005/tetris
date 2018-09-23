import pygame
from random import randint

class Brick():

    def __init__(self,board):
        self.board=board
        self.block_size=board.block_size
        self.accelerated=False
        rand=randint(0,6)
        if rand==0:
            # square
            self.point=[[0,0],[0,1],[1,0],[1,1]]
        elif rand==1:
            # stick
            self.point=[[0,0],[1,0],[2,0],[3,0]]
        elif rand==2:
            # t
            self.point=[[1,0],[0,1],[1,1],[2,1]]
        elif rand==3:
            # left l
            self.point=[[1,0],[1,1],[0,2],[1,2]]
        elif rand==4:
            # right l
            self.point=[[0,0],[0,1],[0,2],[1,2]]
        elif rand==5:
            # left dog
            self.point=[[0,0],[1,0],[1,1],[1,2]]
        elif rand==6:
            # right dog
            self.point=[[1,0],[2,0],[1,1],[0,1]]

        self.x=0
        self.y=0
        self.speed=1
        self.rotation_matrix=[[0,-1],[1,0]]

    def draw(self):
        for point in self.point:
            pygame.draw.rect(pygame.display.get_surface(),(255,255,200),pygame.Rect(self.x*self.block_size+self.board.x+point[0]*self.block_size,self.y+self.board.y+point[1]*self.block_size,self.block_size,self.block_size))
        pygame.display.flip()

    def move_down(self):
        if self.accelerated:
            self.y+=10*self.speed
        else:
            self.y+=self.speed

    def move_left(self):
        flag=False
        for i in range(len(self.point)):
            if self.x-1>=0:
                flag=True
            else:
                flag=False
        if flag:
            self.x-=1

    def move_right(self):
        flag=False
        for i in range(len(self.point)):
            if self.x+1+self.point[i][0]<self.board.width:
                flag=True
            else:
                flag=False
        if flag:
            self.x+=1

    def accelerate(self):
        self.accelerated=True

    def stop_accelerate(self):
        self.accelerated=False

    def rotate(self):
        position_x=[]
        position_y=[]
        for i in range(len(self.point)):
            position_x.append(self.rotation_matrix[0][0]*self.point[i][0]+self.rotation_matrix[0][1]*self.point[i][1])
            position_y.append(self.rotation_matrix[1][0]*self.point[i][0]+self.rotation_matrix[1][1]*self.point[i][1])
        can_rotate=True
        for i in range(len(self.point)):
            if self.x+position_x[i]<0:
                can_rotate=False
                break
        if can_rotate:
            for i in range(len(self.point)):
                self.point[i][0]=position_x[i]
                self.point[i][1]=position_y[i]
