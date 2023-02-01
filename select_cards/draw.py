

from .obj import *
from main import WIN, CANVAS_SIZE
import cls, copy, random, delta_time
from .drop_card import *
import delta_time

def draw_scene():
    WIN.fill(cls.COL.white.value)

    # background_copy = copy.copy(background)

    # background_copy.width /= background.width / WIN.width
    # background_copy.height /= background.width / WIN.width

    # print(f"{background.width} / {WIN.width} = {background.width / WIN.width}")
    # print(f"bg width: {background_copy.width}")
    # print(f"bg height: {background_copy.height}")

    WIN.draw_one(background, 1920)
    WIN.draw_one(left_button, 1920)

    WIN.draw_many([cards_background_border, cards_background], 1920)
    WIN.draw_many([left_button, right_button, head_text, page_text, start_game_button], 1920)

    WIN.draw_many(drop_areas, 1920)
    
    WIN.draw_many(selectable_cards[current_page.value], 1920, True)

    # WIN.draw_one(Text(1650, 10, 70, COL.black.value, f"fps: {str(round(delta_time.average_fps, 2))}"), 1920)
