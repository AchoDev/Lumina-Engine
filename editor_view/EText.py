
import pygame
from .EditorComponent import EditorComponent

class EText(EditorComponent):
    def __init__(self, text, size, color=(255, 255, 255)):
        super().__init__()
        self.text = text
        self.size = size
        self.color = color
        self.font = 'lucidasanstypewriter'

    def get_height(self):
        return self.size
    
    def get_width(self):
        return self.size * len(self.text)
        
    def get_surface(self):
        font = pygame.font.SysFont('lucidasanstypewriter', self.size)
        return font.render(self.text, 1, self.color)
