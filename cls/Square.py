
from os import stat
import pygame
from .GameObject import GameObject

class Square(GameObject):
    def __init__(self, xPos, yPos, width, height, color, border_radius=0, hollow=False):
        super().__init__(xPos, yPos, width, height)

        self.color = color
        self.border_radius = border_radius
        self.is_hollow = hollow

    def draw(self, window):
        window.draw_rect(self, self.color)

    @staticmethod
    def get_square(object):
        return Square(object.x, object.y, object.width, object.height, (0, 0, 0))

    @staticmethod
    def draw_square(object, color, window):
        window.draw_rect(Square.get_square(object), color)
    
    @staticmethod
    def draw_hollow_square(object, color, window):
        obj = Square.get_square(object)
        obj.is_hollow = True
        window.draw_rect(obj, color)