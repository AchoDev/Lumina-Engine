
from .Component import Component

class Transform(Component):
    def __init__(self, xPos, yPos, width, height):
        self.x = xPos
        self.y = yPos
        self.width = width
        self.height = height

    def set(self, obj):
        self.x = obj.x
        self.y = obj.y
        self.width = obj.width
        self.height = obj.height

    
        