
import pygame
from .EditorComponent import EditorComponent
from .collidepoint import collidepoint

class EButton(EditorComponent):
    def __init__(self, text, width, height):
        super().__init__()
        self.text = text
        self.width = width
        self.height = height

        self.clicked = False
        self.hovered = False

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if(collidepoint(mouse_pos, (self.x, self.y, self.width, self.height))):
            self.hovered = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            self.hovered = False
            if(pygame.mouse.get_cursor().data[0] == pygame.SYSTEM_CURSOR_HAND):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def get_surface(self):

        white = (255, 255, 255)
        black = (0, 0, 0)

        back = pygame.Surface((self.width, self.height))
        back.fill(white)

        font = pygame.font.SysFont('lucidasanstypewriter', 15)
        back.blit(font.render(self.text, 1, black), (0, 0))

        return back
    