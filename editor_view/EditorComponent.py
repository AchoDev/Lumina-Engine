
from abc import abstractmethod
import pygame

class EditorComponent:
    
    @abstractmethod
    def get_surface(self) -> pygame.surface:
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

    def get_x(self):
        return 0

    @abstractmethod
    def update(self):
        pass