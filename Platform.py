import pygame

from Color import WHITE

class Platform :
    def __init__(self,x,y,width,height) :
        self.rect=pygame.Rect(x,y,width,height)

    def update(self,win) :
        pygame.draw.rect(win,WHITE,self.rect)