
from .GameObject import GameObject
from components.Transform import Transform

class Camera(GameObject):
    def __init__(self, xPos, yPos, width, height):
        super().__init__(xPos, yPos, width, height)
        self.orthographic_size = 10
        self.original_transform = Transform(xPos, yPos, width, height)

    def change_ortho(self, value):
        self.orthographic_size = value
        