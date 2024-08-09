
from cls.GameObject import GameObject

class Canvas(GameObject):
    def __init__(self):
        super().__init__(0, 0, 100, 100)
        

    def update(self):
        cam_tr = self.scene.camera.transform

        self.x = cam_tr.x
        self.y = cam_tr.y
        self.height = self.scene.camera.orthographic_size * 2
        self.width = self.scene.camera.orthographic_size * 2 * (self.scene.camera.width / self.scene.camera.height)
