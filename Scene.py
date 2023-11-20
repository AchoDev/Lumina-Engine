from main import WIN
from Eventloop import Eventloop
from cls.functions import *
from cls import GameObject, Container, Square, Text, Colors, Camera

from events.KeyEvent import KeyEvent

from components.Draghandler import Draghandler
from components.Transform import Transform


from Box2D import *

import pygame

# class Debug_Variable:
#     def __init__(self, contianer):


# class Debug_Window(GameObject):
#     def __init__(self, title, alpha = 200):
#         super().__init__(100, 100, 200, 500)

#         self.objects = []
#         self.title = title
#         self.alpha = alpha

#         self.__title_text = Text.with_transform(self.title, Transform(0, 0, self.transform.width, self.transform.height), Colors.white)

#         self.box = Square.with_transform(self.transform)
#         self.box.transform.reset_position()
#         self.box.alpha = self.alpha

#         self.add_component(Draghandler(self))

#         self.add_children([self.__title_text, self.box])

#     def draw(self):
#         WIN.value.draw_one(self.box)
#         WIN.value.draw_one(self.__title_text)


# class Object_List(Debug_Window):
#     def __init__(self, title, alpha=200, objects=[]):
#         super().__init__(title, alpha)
#         self.objects = objects
#         self.set_objects()
        

#     def set_objects(self):
#         box_height = 50
#         for i in range(len(self.objects)):
#             text_object = Text.with_transform(self.objects[i].__class__.__name__, self.transform, Colors.white)
#             text_object.transform.reset_position()
#             text_object.transform.y = (i + 1) * box_height
#             self.add_child(text_object)

class Scene:
    def __init__(self, name, objects=[]):

        self.name = name
        self.objects = objects
        self.physics_world = b2World(gravity=(0,10), doSleep=True)
        self.event_loop = Eventloop(self.physics_world)
        self.background_color = (255, 255, 255)

        self.window_dimensions = Container((0, 0))

        self.camera = self.add_object(Camera(0, 0, *WIN.canvas_size))

        self.debug_mode = False
        # self.debug_window = Object_List("Object List", objects=self.objects)

        def toggle_debug():
            self.debug_mode = not self.debug_mode

        self.add_event(KeyEvent(pygame.K_9, toggle_debug))

    def get_window_ratio(self):
        return WIN.get_ratio()
    

    def load(self):

        if self.debug_mode:
            self.debug_window.refresh_components()
            self.debug_window.update()

        for object in self.objects:
            object.refresh_components(self)
            object.update()

        
        WIN.fill(self.background_color)
        # WIN.draw_one(Square(
        #     self.camera.transform.x,
        #     self.camera.transform.y, 
        #     self.camera.orthographic_size, 
        #     self.camera.orthographic_size, 
        #     self.background_color), 
        #     self.camera)

        self.update_dimensions()

        self.camera.original_transform.set(self.camera.transform)

        self.camera.transform.x += self.camera.orthographic_size / 2
        self.camera.transform.y += self.camera.orthographic_size / 2

        WIN.draw_many(self.objects, self.camera)

        self.camera.transform.set(self.camera.original_transform)

        if self.debug_mode:
            self.debug_window.draw()

        self.event_loop.update()

    def update_dimensions(self):
        self.window_dimensions.change((WIN.width, WIN.height))

    def add_event(self, event):
        self.event_loop.add_event(event)
        return event

    def add_many_events(self, events):
        for event in events:
            self.event_loop.add_event(event)
    
    def add_object(self, obj):
        self.objects.append(obj)
        return obj
    
    def add_multiple_objects(self, objs):
        self.objects += objs
        return objs

    def fill(self, color):
        self.background_color = color

    def ADD_PHYSICS_CUBE(self, position):
        body = self.physics_world.CreateDynamicBody(position=(0, 0))
        box = body.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)
        return body
