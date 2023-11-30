

import pygame, copy, sys
from .Container import Container
from .Square import Square
from . import Colors
from .Text import Text

sys.path.append("..")

from components.Transform import Transform
from delta_time import average_fps

window_ratio = Container(100)

debug_mode = Container(False)
class Window:
    def __init__(self, width, height, canvas_size, init=True):
        self.width = width
        self.height = height

        if init: 
            self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)
            pygame.display.set_caption('Lumina-Engine window')
        self.canvas_size = canvas_size

        self.current_camera = None

        window_ratio.change(self.width / self.canvas_size[0])

    def draw_many(self, objects, camera):
        for object in objects:
            # self.win.blit(object.get_body(), (object.x, object.y))
            self.draw_one(object, camera)

    def draw_one(self, obj, camera):
        if(obj == camera): return


        self.current_camera = camera
        window_ratio.change(self.width / self.current_camera.orthographic_size)
        

        ratio = window_ratio.value # l + ratio
        
        if type(obj).__name__ == "Text":
            original_font_size = obj.font_size
            obj.font_size = int(obj.font_size * ratio)             
        
            
        obj.update()
        obj_tf = obj.transform

        ot = Transform.from_transform(obj.transform) # ot -> original transform

        obj_tf.x += self.current_camera.transform.x
        obj_tf.y += self.current_camera.transform.y

        obj_tf.x -= obj_tf.width / 2
        obj_tf.y -= obj_tf.height / 2
# 
        obj_tf.x *= ratio
        obj_tf.y *= ratio
        
        obj_tf.width *= ratio
        obj_tf.height *= ratio

        obj.draw(self)

        obj.transform.set(ot)

        for child in obj.children:
            child_ot = copy.copy(child.transform)
            child_t = child.transform
            child_t.x += obj_tf.x
            child_t.y += obj_tf.y
            child_t.width += obj_tf.width
            child_t.height += obj_tf.height

            self.draw_one(child, camera)

            child.transform.set(child_ot)
            

        if type(obj).__name__ == "Text":
            obj.font_size = original_font_size

    def update(self):
        pass

    def draw_rect(self, obj, color, alpha=255):
        t = obj.transform
        
        if alpha == 255 and t.angle == 0:
            rect = pygame.Rect(t.x, t.y, t.width, t.height)
            pygame.draw.rect(self.win, color, rect, 2 if obj.is_hollow else 0 ,border_radius=obj.border_radius)
        else:
            s = pygame.Surface((t.width, t.height), pygame.SRCALPHA)
            s.set_alpha(alpha)
            s.fill(color)
            s = pygame.transform.rotate(s, -t.angle)
                    
            self.win.blit(s, (t.x, t.y))

    def draw_transparent_square(self, obj, color, alpha):
        s = pygame.Surface((obj.width, obj.height), pygame.SRCALPHA)
        s.set_alpha(alpha)
        s.fill(color)
        self.win.blit(s, (obj.x, obj.y))

    def draw_text(self, text, color, pos, font_size, font, bold=False):
        font = pygame.font.SysFont(font, font_size, bold)
        self.win.blit(font.render(text, 1, color), pos)

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

        self.current_camera.transform.width = self.width
        self.current_camera.transform.height = self.height

        # window_ratio.change(self.width / self.current_camera.transform.width / self.current_camera.orthographic_size)

    def set_attr(self, scale, canvas):
        self.width = scale[0]
        self.height = scale[1]
        self.canvas_size = canvas

        self.win = pygame.display.set_mode(scale, pygame.RESIZABLE, 0)
        pygame.display.set_caption('Lumina-Engine window')


    def get_ratio(self):
        return window_ratio

    @classmethod
    def empty_window(cls):
        return cls(100, 100, (100, 100), init=False)

    @staticmethod
    def get_relative_value(tup):
        return (tup[0] * window_ratio.value, tup[1] * window_ratio.value)

    @staticmethod
    def get_rect(object):
        tr = object.transform
        return pygame.Rect(tr.x, tr.y, tr.width, tr.height)