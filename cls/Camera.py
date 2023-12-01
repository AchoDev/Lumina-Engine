
from .GameObject import GameObject
from components.Transform import Transform
from components.Vector2 import Vector2

class Camera(GameObject):
    def __init__(self, xPos, yPos, width, height):
        super().__init__(xPos, yPos, width, height)
        self.orthographic_size = 100


    def change_ortho(self, value):
        self.orthographic_size = value

    def window_to_world_position(self, pos) -> Vector2:
        
        winPosX = ((pos.x - self.transform.width / 2) / self.transform.width) * self.orthographic_size - self.transform.x
        
        ratio = self.transform.width / (self.transform.height / (self.orthographic_size * 2))
        winPosY = ((pos.y - self.transform.height / 2) / self.transform.height) * ratio - self.transform.y

        return Vector2(winPosX, winPosY)
        