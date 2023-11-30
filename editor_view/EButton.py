
import pygame
from .EditorComponent import EditorComponent

class EButton(EditorComponent):
    def __init__(self, text, width, height):
        super().__init__()
        self.text = text
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def update(self):
        if 

    def get_surface(self):

        white = (255, 255, 255)
        black = (0, 0, 0)

        back = pygame.Surface((self.width, self.height))
        back.fill(white)

        font = pygame.font.SysFont('lucidasanstypewriter', 15)
        back.blit(font.render(self.text, 1, black), (0, 0))

        return back
    