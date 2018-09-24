import pygame
import sys
from Brick import Brick
from Board import Board

class Game():

    def __init__(self):
        self.board=Board()
        self.active_brick=Brick(self.board)
        self.still_brick=[]
        self.start()



    def start(self):
        pygame.display.get_surface().fill((0,0,0))
        self.board.draw()
        self.run()

    def run(self):
        fps_clock=pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        self.active_brick.accelerate()
                    elif event.key==pygame.K_RIGHT:
                        self.active_brick.move_right()
                    elif event.key==pygame.K_LEFT:
                        self.active_brick.move_left()
                    elif event.key==pygame.K_SPACE:
                        self.active_brick.rotate()
                    elif event.key==pygame.K_ESCAPE:
                        pygame.time.wait(10000)
                        print "pause"
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_DOWN:
                        self.active_brick.stop_accelerate()
            self.clear_screen()
            self.board.draw()

            for brick in self.still_brick:
                # removing empty bricks
                if len(brick.point)==0:
                    self.still_brick.remove(brick)
                    break

                # checking if break can go down a
                if self.board.move_brick_down(brick):
                    brick.move_down()
                brick.draw()
            # checink if row is full
            check_row=self.board.check_row()
            if check_row!=False:
                for brick in self.still_brick:
                    brick.remove_element(check_row)
            if self.board.move_brick_down(self.active_brick):
                self.active_brick.draw()
                self.active_brick.move_down()
            else:
                self.still_brick.append(self.active_brick)
                self.active_brick=Brick(self.board)

            fps_clock.tick(30)

    def clear_screen(self):
        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),pygame.Rect(0,0,pygame.display.get_surface().get_size()[0],pygame.display.get_surface().get_size()[1]))
