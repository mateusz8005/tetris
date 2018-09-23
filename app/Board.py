import pygame

class Board():

    def __init__(self):
        self.width=10
        self.height=24
        self.block_size=20
        self.bg_color=(50,50,50)


    def draw(self):
        width=self.width*self.block_size
        height=self.height*self.block_size
        pygame.draw.rect(pygame.display.get_surface(),self.bg_color,pygame.Rect((pygame.display.get_surface().get_size()[0]-width)/2,(pygame.display.get_surface().get_size()[1]-height)/2,width,height))
        pygame.display.flip()
