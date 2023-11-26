from .Component import Component
from .Vector2 import Vector2
import sys

import delta_time

from Box2D import b2Fixture, b2Body

sys.path.append("..")

class Rigidbody(Component):
    def __init__(self):
        super().__init__()
        self._density = 10
        self.fixture: b2Fixture = None
        self.body: b2Body = None 


    def initialize(self):
        self.fixture = self.target.b2Body.fixtures[0]
        self.body = self.target.b2Body
        self.fixture.density = self._density

        self.body.type = 2

        self.body.active = True
        del self._density


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
        self.body.linearVelocity.Set((position.x - tr.x) * fps, (position.y - tr.y) * fps)
        self.body.position.Set(position.x, position.y)


    def add_force(self, force):
        self.xVel += force / self.mass

        self.b2box
