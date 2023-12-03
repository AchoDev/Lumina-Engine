import pygame
from .EditorComponent import EditorComponent

class ECenter(EditorComponent):
    def __init__(self, child: EditorComponent):
        super().__init__()

        self.child: EditorComponent = child

    def update(self, mouse_event):
        self.child.update(mouse_event)

    def get_height(self):
        return self.child.get_height()

    def get_surface(self, editor_width):
        child_x = editor_width / 2 - self.child.get_width() / 2
        self.child.x = child_x
        self.child.y = self.y
        back = pygame.Surface((editor_width, self.child.get_height(), ), pygame.SRCALPHA)
        back.blit(self.child.get_surface(editor_width), (child_x, 0))
        return back