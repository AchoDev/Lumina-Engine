
from os import stat
import pygame
from .GameObject import GameObject

class Square(GameObject):
    def __init__(self, xPos, yPos, width, height, color=(0, 0, 0), border_radius=0, hollow=False, alpha=255):
        super().__init__(xPos, yPos, width, height)

        self.alpha = alpha
        self.color = color
        self.border_radius = border_radius
        self.is_hollow = hollow

    def draw(self, window):
        super().draw(window)
        window.draw_rect(self, self.color, self.alpha)
        self.draw_children(window)

    @staticmethod
    def get_square(object):
        t = object.transform
        return Square(t.x, t.y, t.width, t.height, (0, 0, 0))

    @staticmethod
    def draw_square(object, color, window):
        window.draw_rect(Square.get_square(object), color)
    
    @staticmethod
    def draw_hollow_square(object, color, window):
        obj = Square.get_square(object)
        obj.is_hollow = True
        window.draw_rect(obj, color)