
import os, sys, pygame
CANVAS_SIZE = (1920, 1080)
from cls.Container import Container
WIN = Container()

from cls.Window import Window
from Scene import Scene

pygame.init()

info = pygame.display.Info()

SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

# WIN = Window(1920 / 1, 1080 / 1)
# WIN = Window(2560, 1600)


# 1300
# 800
# 1440, 900
# 2560, 1600


FPS = 60



def init(window_dimensions):

    WIN.value = Window(window_dimensions[0], window_dimensions[1])

    clock = pygame.time.Clock()

    clock.tick(FPS)



if __name__ == "__main__":
    init()