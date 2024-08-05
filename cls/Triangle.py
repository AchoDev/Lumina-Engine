
import pygame
from .GameObject import GameObject

class Triangle(GameObject):
    def __init__(self, xPos=0, yPos=0, width=1, height=1, color=(0, 0, 0)):
        super().__init__(xPos, yPos, width, height)
        self.color = color
        self.name = 'Triangle'

    def get_points(self):
        return [(self.transform.x, self.transform.y + self.transform.height), 
                (self.transform.x + self.transform.width, self.transform.y + self.transform.height), 
                (self.transform.x + self.transform.width / 2, self.transform.y)]

    def draw(self, window):
        super().draw(window)
        pygame.draw.polygon(window.win, self.color, self.get_points())