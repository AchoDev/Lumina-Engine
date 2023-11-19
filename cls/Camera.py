
from .GameObject import GameObject

class Camera(GameObject):
    def __init__(self, xPos, yPos, width, height):
        super().__init__(xPos, yPos, width, height)
        