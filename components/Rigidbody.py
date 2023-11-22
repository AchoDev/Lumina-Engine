from .Component import Component
from .Vector2 import Vector2
import sys

import delta_time

sys.path.append("..")

class Rigidbody(Component):
    def __init__(self, static):
        self.static = static

        self.density = 10
        self._fixed_rotation = False
        self.b2box = None
        

    @property
    def fixed_rotation(self):
        return self._fixed_rotation
    
    @fixed_rotation.setter
    def fixed_rotation(self, rotation):
        self._fixed_rotation = rotation
        if(self.b2box != None):
            self.b2box.fixedRotation = rotation

    @property 
    def velocity(self):
        if(self.b2box == None): 
            return (0, 0)
        
        vel = self.b2box.linearVelocity
        return Vector2(vel.x, vel.y)


    def update(self, scene):

        if not self.b2box:

            tr = self.target.transform
            
            if not self.static: 
                self.b2box = scene.physics_world.CreateDynamicBody(position=tr.get_position())
                self.b2box.fixedRotation = self.fixed_rotation
            else: 
                self.b2box = scene.physics_world.CreateStaticBody(position=tr.get_position())
                self.b2box.fixedRotation = self.fixed_rotation


            w = tr.width / 2
            h = tr.height / 2
            self.b2box.CreatePolygonFixture(box=(w, h), density=1, friction=1.3)


        self.target.transform.set_rotation_rad(self.b2box.angle)
        self.target.transform.set_position(self.b2box.position)

        # self.yVel += (self.gravity * self.grav_multiplier) * delta_time.DELTA_TIME

        # self.transform.x += self.xVel * delta_time.DELTA_TIME
        # self.transform.y += self.yVel * delta_time.DELTA_TIME

    def fix_rotation(self):
        self.fixed_rotation = True

    def move_position(self, position):
        if(self.b2box == None): return
        tr = self.target.transform
        fps = delta_time.get_fps()
        self.b2box.linearVelocity.Set((position.x - tr.x) * fps, (position.y - tr.y) * fps)
        self.b2box.position.Set(position.x, position.y)
        # tr.set_position(position)
        # self.b2box.setLinearVelocity.y = position.y - tr.y

        # print(position.x)
        # print(tr.x)

        # print(self.b2box.linearVelocity)

        # print()

    def add_force(self, force):
        self.xVel += force / self.mass

        self.b2box
