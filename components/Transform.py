
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

        self.parent = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, xPos):
        self._x = xPos
        self.update_b2_position()

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, yPos):
        self._y = yPos
        self.update_b2_position()

    @property
    def width(self):
        return self._width
    
    @width.setter
    def setter(self, w):
        self._width = w
        self.update_b2_position()

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        self._height = h
        self.update_b2_position()

    def set(self, transform):
        # self = copy.copy(transform)

        self.x = transform.x
        self.y = transform.y
        self.width = transform.width
        self.height = transform.height

    def set_parent(self, parent):
        self.parent = parent

    def get_position(self):
        return (self.x, self.y)
    
    def get_scale(self):
        return (self.width, self.height)

    def set_position(self, pos):
        self.x = pos.x
        self.y = pos.y

    def update_b2_position(self):
        if(self.parent != None):
            rb = self.parent.get_component("Rigidbody")

            if(rb == None): return
            if(rb.b2box == None): return
            rb.b2box.position = self.get_position()
            rb.b2pox.cock()

    def set_rotation_rad(self, rad):
        self.angle = rad * (180 / math.pi)

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