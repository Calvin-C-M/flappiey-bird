import pygame
from Color import WHITE

class Player :
    WIDTH=50
    HEIGHT=50
    JUMP_HEIGHT=10

    def __init__(self,x,y) :
        self.rect=pygame.Rect(x,y,self.WIDTH,self.HEIGHT)

    def die(self) :

        return 0

    def update(self,win,grav,ground,keys) :
        # Key Events
        if keys[pygame.K_w] : # Fly
            self.rect.move_ip(0,-self.JUMP_HEIGHT)

        else :
            # Gravity
            if self.rect.colliderect(ground) != True :
                self.rect.move_ip(0,grav)

        pygame.draw.rect(win,WHITE,self.rect)