
import sys

sys.path.append("..")

from cls import GameObject


class Component:
    def __init__(self):
        from .Transform import Transform
        self.target: GameObject = None
        self.transform: Transform = None

    def set_target(self, target: GameObject):
        self.target = target
        self.transform = target.transform

    def editor_repr(self):
        return []

    def update(self, scene):
        pass

    def initialize(self):
        pass

    

    