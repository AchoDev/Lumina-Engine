from .Component import Component
import sys

sys.path.append("..")
import delta_time

class Rigidbody(Component):
    def __init__(self, target, static):
        self.target = target
        self.transform = target.get_component("Transform")
        self.static = static

        self.density = 5

        self.b2box = None
        

    def update(self, scene):

        if not self.b2box:
            if not self.static: self.b2box = scene.physics_world.CreateDynamicBody(position=self.transform.get_position())
            else: self.b2box = scene.physics_world.CreateStaticBody(position=self.transform.get_position())
            
            box = self.b2box.CreatePolygonFixture(box=self.transform.get_scale(), density=1, friction=0.3)

        scene.physics_world.Step(1 / 60, 6, 2)
        scene.physics_world.ClearForces()

        self.target.transform.set_position(self.b2box.position)

        # self.yVel += (self.gravity * self.grav_multiplier) * delta_time.DELTA_TIME

        # self.transform.x += self.xVel * delta_time.DELTA_TIME
        # self.transform.y += self.yVel * delta_time.DELTA_TIME



    def add_force(self, force):
        self.xVel += force / self.mass
