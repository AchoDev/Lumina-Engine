
import pygame
from .EditorComponent import EditorComponent



class EHorizontalList(EditorComponent):
    def __init__(self, children: list[EditorComponent], gap=5, space_evenly=False):
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

        self.space_evenly = space_evenly

        self.width -= self.gap

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def update(self, mouse_event):
        for child in self.children:
            child.update(mouse_event)

    def get_surface(self, editor_width):
        
        current_x = 0

        if(self.space_evenly): 
            self.width = editor_width
            current_x = self.width / len(self.children)
        
        back = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        
        for index, child in enumerate(self.children):
            if(self.space_evenly):
                current_x = (self.width / len(self.children)) * index + 1


            back.blit(child.get_surface(editor_width), (current_x, 0))
            child.x = current_x + self.x
            child.y = self.y

            if(not self.space_evenly):
                current_x += child.get_width()
                current_x += self.gap

            # print(current_x)

            
        return back