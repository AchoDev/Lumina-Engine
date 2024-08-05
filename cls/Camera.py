
from .GameObject import GameObject
from components.Transform import Transform
from components.Vector2 import Vector2

class Camera(GameObject):
    def __init__(self, xPos, yPos, width, height):
        super().__init__(xPos, yPos, width, height)
        self.orthographic_size = 10
        self.name = 'Camera'
        self.window_position: Vector2 = Vector2(0, 0)
        


    def change_ortho(self, value):
        self.orthographic_size = value

    def window_to_world_position(self, pos: Vector2) -> Vector2:
        pixel_per_meter = self.transform.height / (self.orthographic_size * 2)

        winPosX = (pos.x / pixel_per_meter + self.transform.x) - (self.transform.width / pixel_per_meter) / 2
        winPoxY = (pos.y / pixel_per_meter + self.transform.y) - (self.transform.height / pixel_per_meter) / 2

        return Vector2(winPosX, winPoxY)
        