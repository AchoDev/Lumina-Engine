
import pygame, sys

sys.path.append("..")

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

    def update(self, scene):

        if not self.is_draggable: return

        window_ratio = scene.get_window_ratio()

        abs_m_pos = pygame.mouse.get_pos()
        m_pos = abs_m_pos[0] // window_ratio.value, abs_m_pos[1] // window_ratio.value

        if self.is_dragged == True:
            self.pos.x = m_pos[0] - self.__offset[0]
            self.pos.y = m_pos[1] - self.__offset[1]


            if pygame.mouse.get_pressed()[0] == 0:
                self.is_dragged = False
                self.drop()


        tr = self.target.transform
        tr = pygame.Rect(tr.x, tr.y, tr.width, tr.height)

        if tr.collidepoint(m_pos):
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



        
        