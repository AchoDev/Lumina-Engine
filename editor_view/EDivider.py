
import pygame
from .EditorComponent import EditorComponent

class EDivider(EditorComponent):

    def __init__(self, thick=2, margin=5):
        super().__init__()
        self.thick = thick
        self.margin = margin
        self.width = 400

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.thick + self.margin * 2

    def get_surface(self, editor_width):
        self.width = editor_width

        back: pygame.Surface = pygame.Surface((self.width, self.thick + self.margin * 2), pygame.SRCALPHA)
        line = pygame.Surface((self.width, self.thick))
        line.fill(self.white)

        back.blit(line, (0, self.margin))
        return back