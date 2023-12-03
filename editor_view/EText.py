
import pygame
from .EditorComponent import EditorComponent

class EText(EditorComponent):
    def __init__(self, text, size, color=(255, 255, 255)):
        super().__init__()
        self.text = text
        self.size = size
        self.color = color
        self.font = 'lucidasanstypewriter'

        self.font_render = pygame.font.SysFont('lucidasanstypewriter', self.size)

    def get_height(self):
        return self.font_render.size(self.text)[1]
    
    def get_width(self):
        return self.font_render.size(self.text)[0]
        
    def get_surface(self, editor_width):
        return self.font_render.render(self.text, 1, self.color)
