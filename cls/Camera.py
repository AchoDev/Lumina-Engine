
from .GameObject import GameObject
from components.Transform import Transform

class Camera(GameObject):
    def __init__(self, xPos, yPos, width, height):
        super().__init__(xPos, yPos, width, height)
        self.orthographic_size = 10
        self.original_transform = Transform(xPos, yPos, width, height)

    def change_ortho(self, value):
        self.orthographic_size = value

    def window_to_world_position(self, pos):
        
        winPosX = ((pos.x - self.transform.width / 2) / self.transform.width) * self.orthographic_size - self.transform.x
        
        ratio = self.transform.height / (self.transform.width / self.orthographic_size)
        winPosY = ((pos.y - self.transform.height / 2) / self.transform.height) * ratio - self.transform.y

        return Transform(winPosX, winPosY, 0, 0)
        