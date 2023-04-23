
from .GameObject import GameObject
import pygame

class Surface(GameObject):
    def __init__(self, xPos, yPos, surface):
        size = surface.get_size()
        super().__init__(xPos, yPos, *size)
        self.surface = surface

    def draw(self, window):
        self.surface = pygame.transform.scale(self.surface, (round(self.transform.width, 0), self.transform.height))
        window.win.blit(self.surface, (self.transform.x, self.transform.y))

    @classmethod
    def from_surface(cls, pos, surface):
        return cls(pos[0], pos[1], surface.get_size()[0], surface.get_size[1])

    