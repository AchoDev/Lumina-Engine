
import os, sys, pygame
from cls.Window import Window

WIN = Window.empty_window()

pygame.init()
FPS = 60

def init(window_dimensions, fullscreen=False):

    # if not canvas_size: canvas_size = window_dimensions

    WIN.set_attr(window_dimensions, window_dimensions)

    if fullscreen:
        WIN.set_fullscreen()

    clock = pygame.time.Clock()

    clock.tick(FPS)

    return WIN