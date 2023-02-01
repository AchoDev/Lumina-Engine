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

        # self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert()

    def resize(self, width, height):
        self.width = width
        self.height = height

        if self.image != None:
            self.image = pygame.transform.scale(self.image, (width, height))

    def get_image(self):
        return self.image

    def update(self):
        self.image = pygame.image.load(self.path).convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert()

    def draw(self, window):
        window.win.blit(self.image, (self.x, self.y))

    @classmethod
    def with_args(cls, xPos, yPos, width, height):
        img = cls()

        img.set_x(xPos)
        img.set_y(yPos)
        img.width = width
        img.height = height

        return img