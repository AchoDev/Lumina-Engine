
import pygame
from .EditorComponent import EditorComponent
from . import ECenter, EText, EDivider, ECenter

class EInspector(EditorComponent):
    def __init__(self):
        super().__init__()
        self.selected_object = None
        self.height = 300

    def get_height(self):
        return self.height
    
    def get_surface(self, editor_width):

        card_color = (50, 50, 50)
        margin = 10

        back = pygame.Surface((editor_width, self.height), pygame.SRCALPHA)
        
        back.blit(EDivider(margin=0).get_surface(editor_width), (0, 0))

        head_text = ECenter(EText('Inspector', 20))
        back.blit(head_text.get_surface(editor_width), (0, 30))


        if(self.selected_object == None):
            back.blit(ECenter(
                EText('Select an object to inspect it', 15)
            ).get_surface(editor_width), (0, 60))

            return back

        editor_width = editor_width - margin * 2

        current_y = 50 + head_text.child.font_render.size('Inspector')[1]
        for component in self.selected_object.components:
            text = EText(component.__class__.__name__, 18)
            card_height = text.get_height()
            editor_components = component.editor_repr()

            for editor_comp in editor_components:
                card_height += editor_comp.get_height()
            
            card = pygame.Surface((editor_width, card_height), pygame.SRCALPHA)
            card.fill(card_color)
            card.blit(text.get_surface(editor_width), (0, 0))

            current_card_y = text.font_render.size(text.text)[1]
            for editor_component in editor_components:
                card.blit(editor_component.get_surface(editor_width), (0, current_card_y))

                current_card_y += editor_component.get_height()

               
            # c = pygame.Surface((200, 76))
            # # c.fill(self.red)
            # print(back.blit(c, (0, 0)))

            back.blit(card, (margin, current_y))
            current_y += current_card_y

        return back
            