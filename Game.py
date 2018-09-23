import pygame
import sys
from Brick import Brick
from Board import Board

class Game():

    def __init__(self):
        self.board=Board()
        self.active_brick=Brick(4*self.board.block_size)
        self.start()


    def start(self):
        pygame.display.get_surface().fill((0,0,0))
        self.board.draw()
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
