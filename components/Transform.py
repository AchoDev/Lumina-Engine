
from .Component import Component
from .Vector2 import Vector2
import copy
import math

class Transform(Component):
    def __init__(self, xPos, yPos, width, height):
        self._x = xPos
        self._y = yPos
        self._width = width
        self._height = height
        
        self._angle = 0

        self.b2Body = None

    def set_target(self, target):
        self.target = target

        if(self.target.b2Body == None): return

        self.b2Body = target.b2Body
        self.b2Body.position.Set(self._x, self._y)
        

    @property
    def x(self):
        if(self.b2Body == None):
            return self._x
        return self.b2Body.position.x

    @x.setter
    def x(self, xPos):
        if(self.b2Body == None):
            self._x = xPos
            return
        
        self.b2Body.position.Set(xPos, self.b2Body.position.y)

        
    @property
    def y(self):
        if(self.b2Body == None):
            return self._y
        return self.b2Body.position.y
    
    @y.setter
    def y(self, yPos):
        if(self.b2Body == None):
            self._y = yPos
            return
        self.b2Body.position.Set(self.b2Body.position.x, yPos)

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height

    @property
    def angle(self):
        if(self.b2Body == None):
            return self._angle
        return self.b2Body.angle * (180 / math.pi)
    
    @angle.setter
    def angle(self, angle):
        if(self.b2Body == None):
            self._angle = angle
            return
        self.b2Body.angle = angle * (math.pi / 180)

    @property
    def position(self) -> Vector2:
        return Vector2(self.x, self.y)
    
    @position.setter
    def position(self, pos):
        self.x = pos.x
        self.y = pos.y

    def set(self, transform):
        # self = copy.copy(transform)

        self.x = transform.x
        self.y = transform.y
        self.width = transform.width
        self.height = transform.height

    def get_position(self):
        return Vector2(self.x, self.y)
    
    def get_size(self):
        return Vector2(self.width, self.height)

    def set_position(self, pos):
        self.x = pos.x
        self.y = pos.y

    def set_rotation_rad(self, rad):
        self.angle = rad * (180 / math.pi)

    def reset_position(self):
        self.x, self.y = 0

    def reset_size(self):
        self.width, self.height = 0
    
    @classmethod
    def from_transform(cls, transform):
        return cls(
            transform.x,
            transform.y,
            transform.width,
            transform.height
        )

    @staticmethod
    def inbetween(trA, trB):

        result = Transform(0, 0, 0, 0)
        result.x = (trA.x + trB.x) / 2
        result.y = (trA.y + trB.y) / 2

        return result

    def repr(self):
        return f'''\n
        pos: \n
        {self.x}
        {self.y}
        '''