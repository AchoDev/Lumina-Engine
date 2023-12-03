
import pygame
from .EditorComponent import EditorComponent

class EInputField(EditorComponent):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def get_surface(self, editor_width):
        back = pygame.Surface((self.width, self.height))
        back.fill(self.white)

        return back