
import sys

sys.path.append("..")

from cls import GameObject



class Component:
    def __init__(self):
        self.target: GameObject = None

    def set_target(self, target: GameObject):
        self.target = target

    def editor_repr(self):
        return []

    def update(self, scene):
        pass

    def initialize(self):
        pass

    

    