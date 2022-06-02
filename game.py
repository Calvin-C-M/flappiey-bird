import pygame
pygame.init()

from Color import BLACK
from Color import WHITE
from Player import Player
from Platform import Platform
from Pipe import Pipe

WIDTH,HEIGHT=1080,640
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappiey Bird")

FPS=60
GRAV_ACC=5

def updateWindow(
    keys,
    platform,
    player,
    tPipe,
    bPipe,
) :
    WIN.fill(BLACK)

    platform.update(WIN)
    player.update(WIN,GRAV_ACC,platform,keys)

    tPipe.update(WIN,player)
    bPipe.update(WIN,player)

    pygame.display.update()
    pygame.display.flip()

def main() :
    clock=pygame.time.Clock()
    gameRunning=True

    ground=Platform(0,HEIGHT-100,WIDTH,20)  
    player=Player((WIDTH-Player.WIDTH)/2,(HEIGHT-Player.HEIGHT)/2)

    PIPE_GAP=player.HEIGHT*3.5

    topPipe=Pipe(WIDTH-100,0,300)
    botPipe=Pipe(WIDTH-100,topPipe.rect.bottom+PIPE_GAP,ground.rect.top-(topPipe.rect.bottom+PIPE_GAP))

    while gameRunning :
        clock.tick(FPS)

        for evt in pygame.event.get() :
            if evt.type == pygame.QUIT :
                gameRunning=False
        
        keys=pygame.key.get_pressed()
        updateWindow(
            keys,
            ground,
            player,
            topPipe,
            botPipe
        )

main()