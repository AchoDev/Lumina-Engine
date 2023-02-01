import pygame




class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)
    
    def get_object(self, object_name):
        pass

    def load(self):
        for object in self.objects:
            object.draw()