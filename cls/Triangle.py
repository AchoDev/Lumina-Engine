
import pygame
from .GameObject import GameObject

class Triangle(GameObject):
    def __init__(self, xPos=0, yPos=0, width=1, height=1, color=(0, 0, 0), angle=0):
        super().__init__(xPos, yPos, width, height)
        self.color = color
        self.name = 'Triangle'
        self.angle = angle

    def get_points(self):
        return [(self.transform.x, self.transform.y + self.transform.height), 
                (self.transform.x + self.transform.width, self.transform.y + self.transform.height), 
                (self.transform.x + self.transform.width / 2, self.transform.y)]

    def draw(self, window):
        super().draw(window)
        pygame.draw.polygon(window.win, self.color, self.rotate_points_around_pivot(self.get_points(), self.angle))

    def rotate_points_around_pivot(self, points, angle):
        pivot = (self.transform.x + self.transform.width / 2, self.transform.y + self.transform.height / 2)
        pp = pygame.math.Vector2(pivot)
        rotated_points = [
            (pygame.math.Vector2(x, y) - pp).rotate(angle) + pp for x, y in points]
        return rotated_points