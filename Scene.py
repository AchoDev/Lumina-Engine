from main import WIN
from Eventloop import Eventloop
from cls.functions import *
from cls import GameObject, Container, Square, Text, Colors, Camera

from events.KeyEvent import KeyEvent

from components.Draghandler import Draghandler
from components.Transform import Transform

import Input

import delta_time

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
        self.physics_world = b2World(gravity=(0,9.81), doSleep=True)
        self.event_loop = Eventloop(self.physics_world)
        self.background_color = (255, 255, 255)

        self.window_dimensions = Container((0, 0))

        self.camera: Camera = self.add_object(Camera(0, 0, *WIN.canvas_size))

        self.debug_mode = False
        # self.debug_window = Object_List("Object List", objects=self.objects)

        self.__previous_mouse_pos = None

        def toggle_debug():
            self.debug_mode = not self.debug_mode
            

    def get_window_ratio(self):
        return WIN.get_ratio()
    
    def mouse_to_window(self):
        return self.camera.window_to_world_position(Input.get_mouse_pos())

    def load(self):

        WIN.current_scene = self

        if(self.__previous_mouse_pos != None):
            current_mouse = Input.get_mouse_pos()
            self.camera.transform.position -= (current_mouse - self.__previous_mouse_pos) * (self.camera.orthographic_size / self.camera.transform.width)

        if(Input.get_mouse()[2]):
            self.__previous_mouse_pos = Input.get_mouse_pos()
        else:
            self.__previous_mouse_pos = None

        self.camera.orthographic_size -= Input.get_mouse_scroll() * (self.camera.orthographic_size / 5)

        
        if self.debug_mode:
            self.debug_window.refresh_components()
            self.debug_window.update()

        for object in self.objects:
            object.refresh_components(self)
            object.update()


        WIN.fill(self.background_color)

        self.update_dimensions()

        WIN.draw_many(self.objects, self.camera)
        
        if self.debug_mode:
            self.debug_window.draw()

        self.event_loop.add_event(KeyEvent('9', lambda: WIN.toggle_editor_view()))

        self.event_loop.update()

        pass

    def update_dimensions(self):
        self.window_dimensions.change((WIN.width, WIN.height))

    def add_event(self, event):
        self.event_loop.add_event(event)
        return event

    def add_many_events(self, events):
        for event in events:
            self.event_loop.add_event(event)
    
    def add_object(self, obj: GameObject):
        self.objects.append(obj)
        obj.initialize(self)
        
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
