import pygame
from cls.GameObject import GameObject

class Image(GameObject):
    def __init__(self):
        super().__init__(0, 0, 0, 0)
        self.image = None
        self.path = None
    
    def set_image(self, path):
        self.path = path
        self.image = pygame.image.load(path)

        self.transform.width, self.transform.height = self.image.get_size()
        
        return self.image

        # self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert()

    def resize(self, width, height):
        self.transform.width = width
        self.transform.height = height
        self.original_size = (width, height)

        if self.image != None:
            self.image = pygame.transform.scale(self.image, (width, height))
            self.update_image()
            print("UPDATED")

    def get_image(self):
        return self.image

    def update(self):
        super().update()

    def update_image(self):
        self.image = pygame.image.load(self.path).convert()
        self.image = pygame.transform.scale(self.image, (self.transform.width, self.transform.height)).convert()

    def set_surface(self, sur):
        self.image = sur
        return self

    def draw(self, window):

        print(self.transform.width, self.transform.height)

        self.resize(self.transform.width, self.transform.height)

        if self.original_size != self.transform.get_size():
            self.update_image()

        window.win.blit(self.image, (self.transform.x, self.transform.y))

    @classmethod
    def with_args(cls, xPos, yPos, width, height):
        img = cls()

        img.set_x(xPos)
        img.set_y(yPos)
        img.width = width
        img.height = height

        return img