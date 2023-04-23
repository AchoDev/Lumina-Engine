import sys, copy

sys.path.append("..")
from components.Transform import Transform

class GameObject:
    def __init__(self, xPos, yPos, width = 0, height = 0):

        self.__animation = None
        self.original_size = [width, height]

        self.local_tranform = Transform(0, 0, 0, 0)

        self.children = []
        self.components = []
        self.components.append(Transform(xPos, yPos, width, height))
        self.transform = self.get_transform()


    def attach_animation(self, animation):
        self.__animation = animation

    def get_transform(self):
        return self.get_component("Transform")

    def draw(self, screen):
        for child in self.children:
            child.draw(screen)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def add_component(self, component):
        self.components.append(component)

    def get_component(self, name:str):
        for component in self.components:
            if component.__class__.__name__ == name: return component

        return False

    def draw_children(self, window):
        for child in self.children:
            window.draw_one(child)

    def refresh_components(self, scene):
        for component in self.components:
            component.update(scene)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def set_transform(self, transform):
        self.x = transform.x
        self.y = transform.y
        self.width = transform.width
        self.height = transform.height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_animation(self):
        return self.__animation

    def add_child(self, obj):

        obj.local_transform = copy.copy(obj.transform)

        obj.transform.x += self.transform.x
        obj.transform.y += self.transform.y

        self.children.append(obj)

    def add_children(self, objs):
        for child in objs:
            self.add_child(child)

    def clear_children(self):
        self.children = []

    def update_animation(self, dt):
        if self.__animation != None:
            if self.__animation.is_finished == True:
                    self.__animation = None
            else:
                self.__animation.update(dt)
            return True
        else:
            return False

    def update(self):
        for child in self.children:
            child.transform.x = self.transform.x + child.local_transform.x
            child.transform.y = self.transform.y + child.local_transform.y

            child.transform.width *= self.original_size[0] / self.transform.width
            child.transform.height *= self.original_size[1] / self.transform.height

    def place_center(self, width, height):
        self.x = width // 2 - self.width // 2
        self.y = height // 2 - self.height // 2

    def place_right(self, width):
        self.x = width - self.width
    
    def place_left(self):
        self.x = 0

    def place_top(self):
        self.y = 0

    def place_bot(self, height):
        self.y = height - self.height

    def place_top_right(self, width):
        self.place_right(width)
        self.place_top()

    def place_bot_left(self, height):
        self.place_left()
        self.place_bot(height)

    def place_bot_right(self, width, height):
        self.place_right(width)
        self.place_bot(height)

    def place_center_left(self, height):
        self.x = 0
        self.y = height // 2 - self.height // 2

    def place_center_right(self, width, height):
        self.x = width - self.width
        self.y = height // 2 - self.height // 2

    @classmethod
    def with_transform(cls, transform):
        return cls(transform.x, transform.y, transform.width, transform.height)
