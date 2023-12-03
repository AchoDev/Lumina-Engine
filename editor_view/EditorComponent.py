
from abc import abstractmethod
import pygame

class EditorComponent:
    
    def __init__(self):
        self.x = 0
        self.y = 0

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.dark_gray = (38, 38, 38)

    @abstractmethod
    def get_surface(self, editor_width) -> pygame.surface:
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def update(self, mouse_event):
        pass