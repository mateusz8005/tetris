import pygame
import os
class Board():

    def __init__(self):
        self.width=10
        self.height=24
        self.block_size=20
        self.bg_color=(50,50,50)
        self.tab=[]
        for i in range(self.width*self.height):
            self.tab.append(0)
        self.pixel_width=width=self.width*self.block_size
        self.pixel_height=self.height*self.block_size
        self.x=(pygame.display.get_surface().get_size()[0]-self.pixel_width)/2
        self.y=(pygame.display.get_surface().get_size()[1]-self.pixel_height)/2


    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(),self.bg_color,pygame.Rect(self.x,self.y,self.pixel_width,self.pixel_height))

    def move_brick_down(self,brick):
        flag=False
        for i in range(len(brick.point)):
            if (brick.y/self.block_size)+1+brick.point[i][1] < self.height :
                if self.tab[((brick.y/self.block_size)+1+brick.point[i][1])*self.width+brick.x+brick.point[i][0]]==0 :
                    flag=True
                else:
                    flag=False
                    break
            else:

                flag=False
                break
        if flag==True:
            return True
        else:
            for i in range(len(brick.point)):
                self.tab[((brick.y/self.block_size)+brick.point[i][1])*self.width+brick.x+brick.point[i][0]]=1
                print self.tab
            os.system("pause")

            return False
