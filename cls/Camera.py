
from .GameObject import GameObject

class Camera(GameObject):
    def __init__(self, xPos, yPos, width, height):
        super().__init__(xPos, yPos, width, height)
        self.orthographic_size = 10

    def change_ortho(self, value):
        self.orthographic_size = value
        