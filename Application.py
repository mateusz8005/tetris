
import pygame
import sys
from MainMenu import MainMenu

class Application():

    def __init__(self):
        self.screen=pygame.display.set_mode((800,500))
        pygame.display.set_caption("Tetris")
        self.main_menu=MainMenu()
        self.main_menu.show()

if __name__=="__main__":
    app=Application()
