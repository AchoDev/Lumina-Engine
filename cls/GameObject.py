import sys, copy

sys.path.append("..")
from components.Transform import Transform
from components.Component import Component

from Box2D import b2PolygonShape, b2Body

class GameObject:
    def __init__(self, xPos=0, yPos=0, width = 1, height = 1):
        self.__animation = None

        self.children = []
        self.components = []
        self.b2Body: b2Body = None
        self.transform: Transform = self.add_component(Transform(xPos, yPos, width, height))

    def initialize(self, scene):
        self.b2Body = scene.physics_world.CreateDynamicBody(
            position=(self.transform.x, self.transform.y),
            shapes=b2PolygonShape(box=self.transform.get_size().to_tuple())
        )
        self.b2Body.type = 0
        self.b2Body.fixtures[0].filterData.categoryBits = 0x0000
        self.b2Body.fixtures[0].filterData.maskBits = 0x0000

        self.transform.set_target(self)

        for component in self.components:
            component.initialize()



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

    def add_component(self, component: Component):
        self.components.append(component)
        component.set_target(self)
        component.initialize()
        return component

    def get_component(self, name:str):
        for component in self.components:
            if component.__class__.__name__ == name: return component

        return None

    def refresh_components(self, scene):
        for component in self.components:
            component.update(scene)


    def set_transform(self, transform):
        self.x = transform.x
        self.y = transform.y
        self.width = transform.width
        self.height = transform.height


    def get_animation(self):
        return self.__animation

    def add_child(self, obj):

        obj.local_transform = copy.copy(obj.transform)

        obj.transform.x += self.transform.x
        obj.transform.y += self.transform.y

        self.children.append(obj)

        return obj

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
        pass

    @classmethod
    def with_transform(cls, transform):
        return cls(transform.x, transform.y, transform.width, transform.height)
