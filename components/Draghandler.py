
import pygame, sys

sys.path.append("..")

from cls.Window import Window as window, window_ratio
from cls.Square import Square

from .Component import Component

class Draghandler(Component):
    def __init__(self, target):
        super().__init__(target)
        self.is_dragged = False
        self.is_draggable = True
        self.is_hovered = False

        self.pos = target.transform

    def drop(self):
        pass

    def update(self):
        if(self.is_draggable):                
            abs_m_pos = pygame.mouse.get_pos()
            m_pos = abs_m_pos[0] // window_ratio.value, abs_m_pos[1] // window_ratio.value

            if self.is_dragged == True:
                self.pos.x = m_pos[0] - self.__offset[0]
                self.pos.y = m_pos[1] - self.__offset[1]


                if pygame.mouse.get_pressed()[0] == 0:
                    self.is_dragged = False
                    self.drop()

            if window.get_rect(self.target).collidepoint(m_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    if self.is_hovered == True:
                        self.__offset = (m_pos[0] - self.pos.x, m_pos[1] - self.pos.y)
                        self.is_dragged = True
                    else:
                        pass
                else:
                    self.is_hovered = True
            else:
                self.is_hovered = False
                self.is_dragged = False



        
        