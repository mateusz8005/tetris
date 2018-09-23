import pygame

class Board():

    def __init__(self):
        self.width=10
        self.height=24
        self.block_size=20
        self.bg_color=(50,50,50)
        self.tab=[self.height*[0]]*self.width
        self.pixel_width=width=self.width*self.block_size
        self.pixel_height=self.height*self.block_size
        self.x=(pygame.display.get_surface().get_size()[0]-self.pixel_width)/2
        self.y=(pygame.display.get_surface().get_size()[1]-self.pixel_height)/2


    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(),self.bg_color,pygame.Rect(self.x,self.y,self.pixel_width,self.pixel_height))

    def move_brick_down(self,brick):
        if (brick.y/self.block_size)+1 < self.height and self.tab[brick.x][int(brick.y/self.block_size)+1]==0 :
            return True
        else:
            self.tab[brick.x][int(brick.y/self.block_size)]=1
            return False
