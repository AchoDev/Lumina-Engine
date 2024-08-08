

import pygame, copy, sys
from .Container import Container
from .Square import Square
from . import Colors
from .Text import Text
from .Camera import Camera
from .Triangle import Triangle

sys.path.append("..")

from components.Transform import Transform
from delta_time import average_fps


from editor_view import *

window_ratio = Container(100)

debug_mode = Container(False)
class Window:
    def __init__(self, width, height, canvas_size, init=True):
        self._width = width
        self._height = height

        self.editor_view = False

        self.__editor_x = 300
        self.__editor_y = 200

        if init: 
            self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)
            pygame.display.set_caption('Lumina-Engine window')
        self.canvas_size = canvas_size

        self.current_camera = None

        window_ratio.change(self.width / self.canvas_size[0])

        # self.toggle_editor_view()

        self.__resize_editor_x = False
        self.__resize_inspector_y = False

        self.__editor_mouse_event = Container()
        self.__editor_selected_object = None

        self.__object_viewer = EObjectViewer()
        self.__inspector = EInspector()

        button_width = 65
        button_height = 25
        text_size = 17

        self.__current_scene = None
        self.__scene_objects = []


        self.__editor_components: list[EditorComponent] = [
            ECenter(
                EText('Lumina Editor-View', 20),
            ),
            EDivider(),
            ECenter(
                EHorizontalList([
                    EText('View ', text_size),
                    EButton('Game', button_width, button_height),
                    EButton('Editor', button_width, button_height),
                ], 20),
            ),
            ECenter(
                EHorizontalList([
                    EText('Mode ', text_size),
                    EButton('Static', button_width, button_height),
                    EButton('Free', button_width, button_height),
                ], 20),
            ),

            EDivider(),

            ECenter(
                EText('Objects in scene', 20)
            ),

            self.__object_viewer,
            self.__inspector,
        ]

    @property
    def current_scene(self):
        return self.__current_scene

    @current_scene.setter
    def current_scene(self, scene):
        self.__current_scene = scene
        self.__scene_objects = scene.objects

    @property
    def width(self):
        # if(self.editor_view): return self._width - self.__editor_x

        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        # if(self.editor_view): return self._height - self.__editor_y

        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height

    def toggle_editor_view(self):
        self.editor_view = not self.editor_view

        # if(self.editor_view):
        #     pygame.display.set_caption('Lumina-Engine Editor View')
        # else:
        #     pygame.display.set_caption('Lumina-Engine window')


    def validate_absolute_position(self, pos):
        x_res = pos[0]
        y_res = pos[1]
        if(self.editor_view):
            # x_res /= self.width / self._width
            # y_res /= self.height / self._height

            x_res -= self.__editor_x
            y_res -= self.__editor_y
            
        return (x_res, y_res)

    def draw_many(self, objects, camera):
        for object in objects:
            if(not object.active): continue
            # self.win.blit(object.get_body(), (object.x, object.y))
            self.draw_one(object, camera)

    def draw_obj_handles(self, tr: Transform):

        if(not self.editor_view): return

        nav_tf = Transform.from_transform(tr)
        
        nav_tf.width = 4
        nav_tf.height = 100
        nav_tf.x += tr.width / 2
        nav_tf.y -= nav_tf.height - tr.height / 2

        triangle_tr = Transform.from_transform(nav_tf)
        triangle_tr.width = 10
        triangle_tr.height = 10
        triangle_tr.x -= triangle_tr.width / 2 - nav_tf.width / 2
        triangle_tr.y -= triangle_tr.height

        Triangle(triangle_tr.x, triangle_tr.y, triangle_tr.width, triangle_tr.height, Colors.green).draw(self)
        Square(nav_tf.x, nav_tf.y, nav_tf.width, nav_tf.height, Colors.green).draw(self)

        Square(tr.x + tr.width / 2, tr.y + tr.height / 2, 100, 4, Colors.red).draw(self)
        Triangle(tr.x + tr.width / 2 + 100, tr.y + tr.height / 2, 10, 10, Colors.red, angle=90).draw(self)


    def draw_one(self, obj, camera: Camera):
        if(obj == camera): return

        self.current_camera = camera
        window_ratio.change(self.height / (self.current_camera.orthographic_size * 2))
        
        ratio = window_ratio.value # l + ratio

        if type(obj).__name__ == "Text":
            original_font_size = obj.font_size
            obj.font_size = int(obj.font_size * ratio)             
        
        obj_tf = obj.transform

        ot = Transform.from_transform(obj.transform) # ot -> original transform

        obj_tf.x -= self.current_camera.transform.x - (self.width / ratio) / 2
        obj_tf.y -= self.current_camera.transform.y - (self.height / ratio) / 2

        obj_tf.x -= obj_tf.width / 2
        obj_tf.y -= obj_tf.height / 2
# 
        obj_tf.x *= ratio
        obj_tf.y *= ratio

        obj_tf.width *= ratio
        obj_tf.height *= ratio

        
        obj.draw(self)

        self.draw_obj_handles(obj_tf)

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

    def __editor_view_transform(self, tr):
        new_tr = Transform.from_transform(tr)
        
        if(self.editor_view):
            ratio = (self.height - self.__editor_y) / self.height

            new_tr.x *= ratio
            new_tr.y *= ratio

            new_tr.x += self.__editor_x
            # new_tr.y -= self.__editor_y

            
            new_tr.width *= ratio
            new_tr.height *= ratio


        return new_tr

    def draw_rect(self, obj, color, alpha=255):
        
        t = self.__editor_view_transform(obj.transform)

        if alpha == 255 and t.angle == 0:
            rect = pygame.Rect(t.x, t.y, t.width, t.height)
            pygame.draw.rect(self.win, color, rect, 2 if obj.is_hollow else 0 ,border_radius=obj.border_radius)
        else:
            s = pygame.Surface(t.get_size().to_tuple(), pygame.SRCALPHA)
            s.set_alpha(alpha)
            s.fill(color)
            s = pygame.transform.rotate(s, -t.angle)
                    
            self.win.blit(s, t.get_position().to_tuple())

    def draw_triangle(self, obj: Triangle):
        t = self.__editor_view_transform(obj.transform)
        points = obj.get_points()
        draw_points = []
        for point in points:
            draw_points.append((point[0] * window_ratio.value, point[1] * window_ratio.value))
        pygame.draw.polygon(self.win, obj.color, draw_points)


    def draw_transparent_square(self, obj, color, alpha):

        tr = self.__editor_view_transform(Transform(obj.x, obj.y, obj.width, obj.height))
        tr = Transform(obj.x, obj.y, obj.width, obj.height)
        s = pygame.Surface(tr.get_size().to_tuple(), pygame.SRCALPHA)
        s.set_alpha(alpha)
        s.fill(color)
        self.win.blit(s, tr.get_position().to_tuple())

    def draw_text(self, text, color, pos, font_size, font, bold=False):
        font = pygame.font.SysFont(font, font_size, bold)

        tr = self.__editor_view_transform(Transform.from_position(pos))
        tr = Transform.from_position(pos)

        self.win.blit(font.render(text, 1, color), tr.get_position().to_tuple())

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

        window_ratio.change(self.width / self.current_camera.transform.width / self.current_camera.orthographic_size)

    def set_attr(self, scale, canvas):
        self.width = scale[0]
        self.height = scale[1]
        self.canvas_size = canvas

        self.win = pygame.display.set_mode(scale, pygame.RESIZABLE, 0, display=0)
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
    
    def __set_editor_selected_object(self, obj):
        self.__editor_selected_object = obj

    def update_editor_view(self):
        if(self.editor_view):
            
            self.__object_viewer.onclick = lambda obj: self.__set_editor_selected_object(obj)
            self.__object_viewer.scene = self.current_scene
            
            self.__inspector.selected_object = self.__editor_selected_object
            self.__inspector.height = self._height - self.__object_viewer.y - self.__object_viewer.get_height()
            self.__inspector.y = self.__object_viewer.y + self.__object_viewer.height

            for component in self.__editor_components:
                component.update(self.__editor_mouse_event)


            resize_wiggle = 10
            resize_wiggle_y = 20
            
            mouse_pos = pygame.mouse.get_pos()
            is_colliding = collidepoint(mouse_pos, (
                self.__editor_x - resize_wiggle / 2, 
                0,
                resize_wiggle,
                self._height
            ))

            is_colliding_inspector = collidepoint(mouse_pos, (
                0, 
                self.__inspector.y - resize_wiggle_y / 2,
                self.__editor_x,
                resize_wiggle
            ))

            if(is_colliding):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
                self.__editor_mouse_event.value = self

                if(pygame.mouse.get_pressed()[0]):
                    self.__resize_editor_x = True
                else:
                    self.__resize_editor_x = False
            elif(self.__editor_mouse_event.value == self):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if(is_colliding_inspector):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
                self.__editor_mouse_event.value = self.__inspector

                if(pygame.mouse.get_pressed()[0]):
                    self.__resize_inspector_y = True
                else:
                    self.__resize_inspector_y = False
            elif(self.__editor_mouse_event.value == self.__inspector):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


            if(self.__resize_editor_x): self.__editor_x = mouse_pos[0]
            if(self.__resize_inspector_y): 
                self.__inspector.y = mouse_pos[1] - resize_wiggle
                self.__object_viewer.height = mouse_pos[1] - self.__object_viewer.y
                self.__inspector.height = self._height - self.__object_viewer.y - self.__object_viewer.get_height()

            self.draw_editor_view()

    def draw_editor_view(self):
        white = (255, 255, 255)
        main_color = (  
           27, 25, 27
        )

        def draw_rect_abs(tr, color=main_color):
            rect = pygame.Rect(tr.x, tr.y, tr.width, tr.height)
            pygame.draw.rect(self.win, color, rect)
        
        draw_rect_abs(
            Transform(0, 0, self.__editor_x, self._height)
        )

        object_viewer = pygame.Surface((self.__editor_x, self._height))
        object_viewer.fill(main_color)


        draw_rect_abs(
            Transform(
                self.__editor_x,
                self._height - self.__editor_y,
                self._width - self.__editor_x,
                self.__editor_y
            )
        )
        pygame.draw.line(self.win, white, (self.__editor_x, self._height - self.__editor_y), (self.__editor_x, self._height), 1)

        current_y = 5

        for component in self.__editor_components:
            component.y = current_y
            object_viewer.blit(component.get_surface(self.__editor_x), (component.x, current_y))

            current_y += component.get_height()
            current_y += 5

        self.win.blit(object_viewer, (0, 0))
