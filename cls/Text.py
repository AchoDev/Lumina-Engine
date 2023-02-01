
import pygame
from cls.GameObject import GameObject
from cls.Square import Square

pygame.font.init()

class Text(GameObject):
    def __init__(self, xPos, yPos, font_size, color, text):
        super().__init__(xPos, yPos)
        
        self.font_size = font_size
        self.font = pygame.font.SysFont('ebrima', font_size)
        self.text = text 
        self.color = color

        # self.width = 1920

        # self.__set_size()
        
    def __set_size(self):
        self.width = self.__get_body().get_width()
        self.height = self.__get_body().get_height()

    def __get_body(self):

        self.font = pygame.font.SysFont('ebrima', self.font_size)
        return self.font.render(self.text, 1, self.color)

    def draw(self, window):
        text = self.font.render(self.text, 1, self.color)
        window.win.blit(self.__get_body(), (self.transform.x, self.transform.y))

        self.__set_size()
        # Square.draw_hollow_square(self, COL.violet.value, window)

    def change_text(self, text):
        self.text = text

    def place_center(self, width, height):
        self.__set_size()
        super().place_center(width, height)