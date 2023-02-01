from main import WIN, CANVAS_SIZE
from Eventloop import Eventloop
from cls.functions import *
from cls.Square import Square
from cls.Container import Container
from events.KeyEvent import KeyEvent

from components.Transform import Transform
from components.Draghandler import Draghandler

import pygame

class Debug_Window:
    def __init__(self): pass

class Scene:
    def __init__(self, name, objects=[]):
        self.name = name
        self.objects = objects
        self.event_loop = Eventloop()
        self.background_color = (255, 255, 255)

        self.window_dimensions = Container((0, 0))

        self.debug_mode = False
        self.debug_objects = [Square(100, 100, 300, 500, (150, 150, 150), 1)]
        self.debug_objects[0].add_component(Draghandler(self.debug_objects[0]))

        def toggle_debug():
            self.debug_mode = not self.debug_mode

        self.add_event(KeyEvent(pygame.K_9, toggle_debug))

    def load(self):

        for object in self.objects + self.debug_objects:
            object.refresh_components()
            object.update()

        
        WIN.value.fill((0, 0, 0))
        WIN.value.draw_one(Square(0, 0, CANVAS_SIZE[0], CANVAS_SIZE[1], self.background_color))

        self.update_dimensions()

        WIN.value.draw_many(self.objects)

        if self.debug_mode:
            WIN.value.draw_many(self.debug_objects)

        self.event_loop.update()

    def update_dimensions(self):
        self.window_dimensions.change((WIN.value.width, WIN.value.height))

    def add_event(self, event):
        self.event_loop.add_event(event)

    def add_many_events(self, events):
        for event in events:
            self.event_loop.add_event(event)
    
    def add_one(self, obj):
        self.objects.append(obj)
    
    def add_many(self, objs):
        self.objects += objs

    def fill(self, color):
        self.background_color = color
