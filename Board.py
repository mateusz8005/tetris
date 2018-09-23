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
        flag=False
        for i in range(0,3):
            if (brick.y/self.block_size)+1+brick.point[i][1] < self.height and self.tab[brick.x+brick.point[i][0] ][int(brick.y/self.block_size)+1+brick.point[i][1]]==0 :
                flag=True
            else:
                flag=False
                break
        if flag==True:
            return True
        else:
            for i in range(0,3):
                self.tab[brick.x+brick.point[i][0]][int(brick.y/self.block_size)+brick.point[i][1]]=1
            return False
