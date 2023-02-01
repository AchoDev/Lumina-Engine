
import os
from cls import *
from .drop_card import check_drop

def get_path(color, image_name):
    image = Image()
    image.set_image(os.path.join("Assets", "Cards", color, image_name + ".jpeg"))

    return image
class Selectable_Card(GameObject, Draggable):
    def __init__(self, color, image_name):
        GameObject.__init__(self, 0, 100, 350, 400)
        Draggable.__init__(self)

        self.original_pos = (self.x, self.y)
        self.original_size = (self.width, self.height)

        self.image = get_path(color, image_name)

        self.__update_once = False

        self.card_values = [color, image_name]

    def set_original_pos(self):
        self.original_pos = (self.x, self.y)

    def drop(self):
        check_drop(self)
            
    def update(self):
        self.drag()

    def sync_image(self):
        sync_transform(self, self.image)

    def update_once(self):
        self.__update_once = True

    def return_to_original_transform(self):
        self.x = self.original_pos[0]
        self.y = self.original_pos[1]

        self.width = self.original_size[0]
        self.height = self.original_size[1]

    def draw(self, window):
        # Draggable.draw(Selectable_Card, self) 
        self.sync_image()

        window.draw_one(Square(*self.original_pos, *self.original_size, COL.white.value, hollow=True), 1920)

        self.image.resize(self.width, self.height)
        self.image.draw(window)

        if self.__update_once:
            self.image.update()
        



