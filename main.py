
import os, sys, pygame
from cls.Window import Window

WIN = Window.empty_window()

pygame.init()
FPS = 60

def init(window_dimensions, canvas_size=None):

    if not canvas_size: canvas_size = window_dimensions

    WIN.set_attr(window_dimensions, canvas_size)

    clock = pygame.time.Clock()

    clock.tick(FPS)

    return WIN