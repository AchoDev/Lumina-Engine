import pygame
from . import Colors
from .Text import Text
from .GameObject import GameObject
from .functions import sync_position, sync_transform




class Button(GameObject):
    def __init__(self, xPos=0, yPos=0, font_size=100, width=100, height=35, 
                color=Colors.white, text="text", event=None, 
                border_radius=0, hollow=False):

        super().__init__(xPos, yPos, width, height)

        self.color = color

        if text != "IMAGE_BUTTON":
            self.text = Text(self.x, self.y, font_size, Colors.black, text)
        
        self.event = event

        self.border_radius = border_radius
        self.is_hollow = hollow

        self.font_size = font_size


        self.clicked = False

        self.__image = None


    def set_image(self, image):
        self.__image = image

    @classmethod
    def image_button(cls, xPos, yPos, width, height, event, image):
        btn = cls(xPos, yPos, 0, width, height, None, "IMAGE_BUTTON", None, event)
        btn.set_image(image)
        btn.update_image()

        return btn

    @classmethod
    def invisible_button(cls):
        return cls(0, 0, 0, 0, None, "", None, None)

    def update_image(self):
        sync_transform(self, self.__image)
        self.__image.update()


    def draw(self, window):

        if self.__image == None:
            window.draw_rect(self, self.color)
            sync_position(self, self.text)
            self.text.font_size = self.font_size
            self.text.draw(window)
        else:
            self.__image.draw(window)
        
        m_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 1:

            if self.clicked == False:
                if window.get_rect(self).collidepoint(m_pos):

                    # print(m_pos, self.x, self.y, self.width, self.height)
                    # print(window.get_rect(self).collidepoint(m_pos))

                    self.clicked = True
                    pygame.event.post(pygame.event.Event(self.event))
                    

        elif pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False