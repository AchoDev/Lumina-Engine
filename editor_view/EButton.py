
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

    def update(self, mouse_event):
        mouse_pos = pygame.mouse.get_pos()

        if(collidepoint(mouse_pos, (self.x, self.y, self.width, self.height))):
            self.hovered = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            mouse_event.value = self

        else:
            self.hovered = False
            if(mouse_event.value == self):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def get_surface(self, editor_width):

        white = (255, 255, 255)
        black = (0, 0, 0)

        back = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        pygame.draw.rect(back, self.white, (0, 0, self.width, self.height), border_radius=2)

        font = pygame.font.SysFont('lucidasanstypewriter', 15)
        text_size = font.size(self.text)

        back.blit(font.render(self.text, 1, black), (self.width / 2 - text_size[0] / 2, self.height / 2 - text_size[1] / 2))

        return back
    