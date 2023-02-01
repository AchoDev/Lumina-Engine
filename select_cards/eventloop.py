
import pygame

from .drop_card import get_cards
from .draw import draw_scene
from .obj import *
from main import WIN
import delta_time
import console, cls, sys

def start():

    console.watch(delta_time.afc, "fps", True)
    console.watch(debug_mode, "debug_mode", True)

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.VIDEORESIZE:
                WIN.videoresize()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:

                    if console.is_visible:
                        console.is_visible = False
                    else:
                        console.is_visible = True

                if event.key == pygame.K_9:
                    if debug_mode.value == True:
                        debug_mode.value = False
                    else:
                        debug_mode.value = True

            if event.type == LEFT_BUTTON_PRESS:

                if current_page.value != 0:
                    current_page.value -= 1
                else:
                    current_page.value = len(selectable_cards) - 1
                page_text.text = f"Page {str(current_page.value + 1)} / {len(selectable_cards)}"
            if event.type == RIGHT_BUTTON_PRESS:

                if current_page.value < len(selectable_cards) - 1:
                    current_page.value += 1
                else:
                    current_page.value = 0
                page_text.text = f"Page {str(current_page.value + 1)} / {len(selectable_cards)}"

            if event.type == START_GAME_EVENT:
                cards = get_cards()
                console.log(str(cards))
                if cards:
                    scene.load_scene(cards)
                


        draw_scene()
        delta_time.update_delta_time()
        console.draw_console()
        
        pygame.display.update()
