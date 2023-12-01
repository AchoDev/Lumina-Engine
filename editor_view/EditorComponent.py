
from abc import abstractmethod
import pygame

class EditorComponent:
    
    def __init__(self):
        self.x = 0
        self.y = 0

    @abstractmethod
    def get_surface(self) -> pygame.surface:
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def update(self):
        pass