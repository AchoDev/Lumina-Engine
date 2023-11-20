
from .Component import Component
from .Vector2 import Vector2
import copy

class Transform(Component):
    def __init__(self, xPos, yPos, width, height):
        self.x = xPos
        self.y = yPos
        self.width = width
        self.height = height

    def set(self, transform):
        # self = copy.copy(transform)

        self.x = transform.x
        self.y = transform.y
        self.width = transform.width
        self.height = transform.height

    def get_position(self):
        return (self.x, self.y)
    
    def get_scale(self):
        return (self.width, self.height)

    def set_position(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def reset_position(self):
        self.x, self.y = 0

    def reset_size(self):
        self.width, self.height = 0

    def get_size(self):
        return self.scale
    
    def repr(self):
        return f'''\n
        pos: \n
        {self.x}
        {self.y}
        '''