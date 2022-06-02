import pygame

from Color import WHITE

class Pipe :
    WIDTH=100
    VEL=3
    
    def __init__(self,x,y,height) :
        self.rect=pygame.Rect(x,y,self.WIDTH,height)

    def stop(self) :
        return 0

    def update(self,win,player) :
        pygame.draw.rect(win,WHITE,self.rect)
        self.rect.move_ip(-self.VEL,0)

        if self.rect.colliderect(player) == True :
            print("Hit")
