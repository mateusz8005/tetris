import pygame

class Button():

    def __init__(self,*args,**kwargs):
        try:
            self.x=kwargs['x']
            self.y=kwargs['y']
            self.width=kwargs['width']
            self.height=kwargs['height']
            self.font_name='comicsansms'
            self.font_size=36
            self.bg_color=(0,200,155)
            self.text_color=(0,50,50)
            self.hover_bg_color=(50,250,200)
            self.hover_text_color=(50,100,100)
            self.active_bg_color=self.bg_color
            self.active_text_color=self.text_color
        except NameError:
            pass
        try:
            self.text=kwargs['text']
        except:
            self.text=None
        self.show()

    def show(self):
        pygame.draw.rect(pygame.display.get_surface(),self.active_bg_color,pygame.Rect(self.x,self.y,self.width,self.height))
        self.show_text()

    def set_text(self,text):
        self.text=text

    def show_text(self):
        pygame.font.init()
        font=pygame.font.SysFont(self.font_name, self.font_size)
        text_surface=font.render(self.text,True,self.active_text_color)
        text_width=len(self.text)*self.font_size
        pygame.display.get_surface().blit(text_surface,(self.x+(self.width-font.size(self.text)[0])/2,self.y+(self.height-font.size(self.text)[1])/2))

    def set_bg_color(self,color):
        self.bg_color=color

    def set_text_color(self,color):
        self.text_color=color

    def hover(self,mouse_pos):
        if mouse_pos[0]>=self.x and mouse_pos[0]<=self.x+self.width and mouse_pos[1]>=self.y and mouse_pos[1]<=self.y+self.height:
            self.active_bg_color=self.hover_bg_color
            self.active_text_color=self.hover_text_color
            self.show()
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            pygame.display.flip()
            return True
        elif self.active_bg_color!=self.bg_color:
            self.active_bg_color=self.bg_color
            self.active_text_color=self.text_color
            self.show()
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            pygame.display.flip()
            return False
