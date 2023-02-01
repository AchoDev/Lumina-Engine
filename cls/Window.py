

import pygame, copy, sys
from .Container import Container
from .Square import Square
from . import Colors
from .Text import Text

sys.path.append("..")

from components.Transform import Transform
from delta_time import average_fps
from main import CANVAS_SIZE

window_ratio = Container(0)

debug_mode = Container(False)
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)
        self.canvas_width = CANVAS_SIZE[0]

        window_ratio.change(self.width / self.canvas_width)

    def draw_many(self, objects, prn=False):
        for object in objects:
            # self.win.blit(object.get_body(), (object.x, object.y))
            self.draw_one(object, prn) 

    def draw_one(self, obj, prn=False):


        
        ratio = window_ratio.value # l + ratio
        
        if type(obj).__name__ == "Text":
            original_font_size = obj.font_size
            obj.font_size = int(obj.font_size * ratio)             
        
            
        obj.update()
        obj_tf = obj.transform

        ot = copy.copy(obj.transform) # ot -> original transform
        

        obj_tf.x *= ratio
        obj_tf.y *= ratio
        
        obj_tf.width *= ratio
        obj_tf.height *= ratio

        obj.draw(self)

        if prn and debug_mode.value:
            # print(obj.width)
            # print(obj.height)
            self.draw_rect(Square(ot.x, ot.y, ot.width, ot.height, Colors.blue, hollow=True), Colors.green)

        obj.transform.set(ot)

        if type(obj).__name__ == "Text":
            obj.font_size = original_font_size


    def draw_rect(self, obj, color):
        rect = pygame.Rect(obj.transform.x, obj.transform.y, obj.transform.width, obj.transform.height)
        pygame.draw.rect(self.win, color, rect, 2 if obj.is_hollow else 0 ,border_radius=obj.border_radius)

    def draw_transparent_square(self, obj, color, alpha):
        s = pygame.Surface((obj.x * window_ratio.value, obj.y * window_ratio.value))
        s.set_alpha(alpha)                
        s.fill(color)           
        self.win.blit(s, (obj.x * window_ratio.value, obj.y * window_ratio.value))

    def draw_line(self, obj, color):
        pygame.draw.line(self.win, color, (obj.x1, obj.y1), (obj.x2, obj.y2), 1)

    def get_rect(self, object):
        return pygame.Rect(object.x, object.y, object.width, object.height)

    def fill(self, color):
        self.win.fill(color)
    
    def get_center(self):
        return [self.width // 2, self.height // 2]

    def videoresize(self):
        self.width = self.win.get_width()
        self.height = self.win.get_height()

        window_ratio.change(self.width / self.canvas_width)

    @staticmethod
    def get_rect(object):
        tr = object.transform
        return pygame.Rect(tr.x, tr.y, tr.width, tr.height)