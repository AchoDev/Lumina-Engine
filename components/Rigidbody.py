from .Component import Component
from .Vector2 import Vector2
import sys

import delta_time

sys.path.append("..")

class Rigidbody(Component):
    def __init__(self, target, static):
        self.target = target
        self.transform = target.get_component("Transform")
        self.static = static

        self.density = 10

        self.b2box = None
        

    def update(self, scene):

        if not self.b2box:
            if not self.static: self.b2box = scene.physics_world.CreateDynamicBody(position=self.transform.get_position())
            else: self.b2box = scene.physics_world.CreateStaticBody(position=self.transform.get_position())

            w = self.transform.width / 2
            h = self.transform.height / 2
            self.b2box.CreatePolygonFixture(box=(w, h), density=1, friction=1.3)


        self.target.transform.set_rotation_rad(self.b2box.angle)
        self.target.transform.set_position(self.b2box.position)

        # self.yVel += (self.gravity * self.grav_multiplier) * delta_time.DELTA_TIME

        # self.transform.x += self.xVel * delta_time.DELTA_TIME
        # self.transform.y += self.yVel * delta_time.DELTA_TIME

    def move_position(self, position):
        if(self.b2box == None): return
        tr = self.target.transform
        fps = delta_time.get_fps()
        self.b2box.linearVelocity.Set((position.x - tr.x * fps), (position.y - tr.y) * fps)
        self.b2box.position.Set(position.x, position.y)
        # tr.set_position(position)
        # self.b2box.setLinearVelocity.y = position.y - tr.y

        # print(position.x)
        # print(tr.x)

        print(self.b2box.linearVelocity)

        # print()

    def add_force(self, force):
        self.xVel += force / self.mass

        self.b2box
