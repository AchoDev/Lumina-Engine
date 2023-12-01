
import pygame
from .EditorComponent import EditorComponent

class EHorizontalList(EditorComponent):
    def __init__(self, children: list[EditorComponent], gap=5):
        super().__init__()
        self.children = children
        self.gap = gap

        self.width = 0
        self.height = self.gap

        for child in self.children:
            if(child.get_height() > self.height):
                self.height = child.get_height()

                self.width += child.get_width()
                self.width += self.gap

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def update(self):
        for child in self.children:
            child.update()

    def get_surface(self):
        
        back = pygame.Surface((self.width, self.height))
        
        current_x = self.gap
        for child in self.children:
            back.blit(child.get_surface(), (current_x, 0))

            child.x = current_x

            current_x += child.get_width()
            current_x += self.gap

        return back