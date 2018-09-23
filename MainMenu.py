import pygame
import sys
from Button import Button
from Game import Game


class MainMenu():

    def __init__(self):
        self.screen=pygame.display.get_surface()
        self.mouse_pos=(0,0)
        self.btn_width=200
        self.btn_height=50
        self.btn_y=100
        surface=pygame.display.get_surface()
        self.btn_x=3*((surface.get_size()[0]-self.btn_width)/4)
        self.button={}
        self.button['play']=Button(x=self.btn_x,y=self.btn_y,width=self.btn_width,height=self.btn_height,text="Play")
        self.button['settings']=Button(x=self.btn_x,y=self.btn_y+2*self.btn_height,width=self.btn_width,height=self.btn_height,text="Settings")
        self.button['exit']=Button(x=self.btn_x,y=self.btn_y+4*self.btn_height,width=self.btn_width,height=self.btn_height,text="Exit")
        self.logo=pygame.image.load("img/logo.png")
        self.logo=pygame.transform.scale(self.logo,(surface.get_size()[0]/2,surface.get_size()[0]/2))

        self.is_active=True


    def show(self):
        pygame.display.get_surface().blit(self.logo,(0,0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.click()
                self.update_mouse_pos(mouse_pos=pygame.mouse.get_pos())


    def update_mouse_pos(self,mouse_pos):
        if self.is_active:
            self.mouse_pos=mouse_pos
            for button in self.button.itervalues():
                button.hover(mouse_pos)

    def click(self):
        if self.is_active:
            if self.button['play'].hover(self.mouse_pos):
                self.is_active=False
                game=Game()

            elif self.button['exit'].hover(self.mouse_pos):
                pygame.quit()
                sys.exit()

    def load_logo(self):
        self.logo=pygame.image.load("img/logo.png")
        self.logo=pygame.transform.scale(self.logo,(surface.get_size()[0]/2,surface.get_size()[0]/2))
        surface.blit(self.logo,(0,0))
