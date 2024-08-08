from .Component import Component
from .Vector2 import Vector2
import sys

import delta_time

from Box2D import b2Fixture, b2Body, b2_staticBody, b2_dynamicBody, b2_kinematicBody

sys.path.append("..")

from editor_view import *

class Rigidbody(Component):
    def __init__(self, static=False):
        super().__init__()
        self._density = 10
        self.fixture: b2Fixture = None
        self.body: b2Body = None 
        self.static = static


    def initialize(self):
        self.fixture = self.target.b2Body.fixtures[0]
        self.body = self.target.b2Body
        self.fixture.density = self._density

        self.body.type = b2_dynamicBody if not self.static else b2_kinematicBody

        self.body.active = True
        del self._density

    def editor_repr(self):
        text_size = 15
        return [
            EHorizontalList(
                [EText('Mass', text_size), EInputField(50, 20)], space_evenly=True
            ),
            EHorizontalList(
                [EText('Linear drag', text_size), EInputField(50, 20)], space_evenly=True
            ),
            EHorizontalList(
                [EText('Angular drag', text_size), EInputField(50, 20)], space_evenly=True
            ),
            EHorizontalList(
                [EText('Gravity scale', text_size), EInputField(50, 20)], space_evenly=True
            ),
        ]

    @property
    def fixed_rotation(self):
        return self.target.b2Body.fixedRotation
    
    @fixed_rotation.setter
    def fixed_rotation(self, rotation):
        self.b2Body.fixedRotation = rotation

    @property 
    def velocity(self):
        if(self.b2box == None):
            return (0, 0)
        
        vel = self.b2box.linearVelocity
        return Vector2(vel.x, vel.y)

    @property
    def density(self):
        return self.fixture.density
    
    @density.setter
    def density(self, density):
        self.fixture.density = density

    def update(self, scene):
        pass    
        # self.b2box.CreatePolygonFixture(box=(w, h), density=1, friction=1.3)

    def fix_rotation(self):
        self.fixed_rotation = True

    def move_position(self, position):
        if(self.body == None): return
        tr = self.target.transform
        fps = delta_time.get_fps()
        self.body.linearVelocity = ((position.x - tr.x) * fps, (position.y - tr.y) * fps)
        
    def smooth_move_to(self, position, speed=5):
        if(self.body == None): return
        tr = self.target.transform
        self.body.linearVelocity = ((position.x - tr.x) * speed, (position.y - tr.y) * speed)

    def add_force(self, force):
        self.xVel += force / self.mass

        self.b2box
