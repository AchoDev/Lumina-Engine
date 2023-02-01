
from main import CANVAS_SIZE as cs
import pygame, sys, os

from .Selectable_Card import Selectable_Card as sc

sys.path.append("..")
sys.path.append("..")
sys.path.append(".")

from cls import *

background = Square(0, 0, 1920, 1080, COL.blue.value)

head_text = Text(0, 0, 120, COL.black.value, "SELECT CARDS")

page_text = Text(100, 100, 100, COL.black.value, "Page 999/6")
page_text.place_center(1920, 1080)
page_text.y = 5


LEFT_BUTTON_PRESS = pygame.USEREVENT + 20
RIGHT_BUTTON_PRESS = pygame.USEREVENT + 21
START_GAME_EVENT = pygame.USEREVENT + 22

start_game_button = Button(0, 0, 40, 330, 130, COL.white.value, "START GAME!", START_GAME_EVENT, 1)
start_game_button.place_bot_right(1920, 1080)

start_game_button.x -= 100
start_game_button.y -= 100

left_button = Button(0, 200, 50, 70, 70, COL.white.value, "<", LEFT_BUTTON_PRESS, 1)
right_button = Button(300, 0, 50, 70, 70, COL.white.value, ">", RIGHT_BUTTON_PRESS, 1)

left_button.place_left()
right_button.place_right(cs[0])

cb_y = 100
cb_height = 400
cb_border_width = 5

left_button.y = cb_y + cb_height // 2 - left_button.height // 2
right_button.y = cb_y + cb_height // 2 - right_button.height // 2

cards_background = Square(0, cb_y, cs[0], cb_height, COL.yellow.value)
cards_background_border = Square(-10, cb_y - cb_border_width, cs[0], cb_height + cb_border_width * 2, COL.black.value)

cards_width = 1000
current_page = Container(0)


selectable_cards = [
    [
        sc("red", "broken_tank"),
        sc("red", "goblin"),
        sc("red", "junkie"),
        sc("red", "lost_ghost")
    ],
    [
        sc("red", "missing_transition"),
        sc("red", "passionate_icecream_eater"),
        sc("red", "sleep_paralysis_demon")
    ],
    [
        sc("blue", "bubblegum_dealer"),
        sc("blue", "kuba_colognalo"),
        sc("blue", "mario"),
        sc("blue", "sad_rejection")
    ],
    [
        sc("blue", "stand_up_comedian")
    ],
    [
        sc("green", "cameraman"),
        sc("green", "desert_bandit"),
        sc("green", "hell_demon"),
        sc("green", "no_way")
    ],
    [
        sc("green", "x_rayvren")
    ]
]

for cards in selectable_cards:
    align_x(1600, cards)
    align_center_x(1920, cards)

    for card in cards:
        card.set_original_pos()

