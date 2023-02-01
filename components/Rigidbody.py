from .Component import Component
import sys

sys.path.append("..")
import delta_time

class Rigidbody(Component):
    def __init__(self, target):
        self.target = target
        self.transform = target.get_component("Transform")
        
        self.gravity = 9.81
        self.grav_multiplier = 150
        self.mass = 5
        
        self.xVel = 0
        self.yVel = 0

    def update(self):
        self.yVel += (self.gravity * self.grav_multiplier) * delta_time.DELTA_TIME

        self.transform.x += self.xVel * delta_time.DELTA_TIME
        self.transform.y += self.yVel * delta_time.DELTA_TIME

    def add_force(self, force):
        self.xVel += force / self.mass
