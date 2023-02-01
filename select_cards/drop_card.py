from cls import *


def check_drop(object):
    for area in drop_areas:
        if Window.get_rect(area).colliderect(Window.get_rect(object)):
            if area.put_card == None:
                object.set_transform(area)
                area.put_card = object
                object.is_draggable = False
                return None
            else:
                object.return_to_original_transform()
    
    object.set_transform(Transform(
        object.original_pos[0],
        object.original_pos[1],

        object.original_size[0],
        object.original_size[1]
    ))



class Drop_Area(GameObject):
    def __init__(self, xPos, yPos, index):
        super().__init__(xPos, yPos, 200, 260)
        self.put_card = None
        self.color = COL.white.value

        self.index = index
        self.clicked = False
        self.is_hovered = False

    def place_card(self, card):
        if self.put_card == None:
            self.put_card = card
        else:
            card.return_to_original_transform()

    def draw(self, window):

        Square(self.x, self.y, self.width, self.height, self.color, 1, True).draw(window)

        m_pos = pygame.mouse.get_pos()
        
        
        if window.get_rect(self).collidepoint(m_pos):

            if pygame.mouse.get_pressed()[0] == 1:

                if self.clicked == False and self.is_hovered == True:

                    self.clicked = True
                    if self.put_card != None:
                        self.put_card.return_to_original_transform()
                        self.put_card.is_draggable = True

                        self.put_card.sync_image()

                        self.put_card.image.update()

                        self.put_card.update_once()

                        self.put_card = None
            else:
                self.clicked = False
                self.is_hovered = True
        else:
            self.is_hovered = False
            self.clicked = False

        if self.put_card != None:
            window.draw_one(self.put_card, 1920)


        
    
drop_areas = [
    Drop_Area(1000, 600, 0),
    Drop_Area(1000, 600, 1),
    Drop_Area(1000, 600, 2),
    Drop_Area(1000, 600, 3),
    Drop_Area(1000, 600, 4),
    Drop_Area(1000, 600, 4),
]

align_grid_center(drop_areas, 700, 550, (1920, 1080), 3)

for area in drop_areas:
    area.y += 260


def get_cards():
    card_list = []
    return [
        drop_areas[0].put_card,
        drop_areas[0].put_card,
        drop_areas[0].put_card,
        drop_areas[0].put_card,
        drop_areas[0].put_card,
        drop_areas[0].put_card
    ]

    for area in drop_areas:
        if area.put_card:
            card_list.append(area.put_card)
        else:
            return None


    # return card_list
