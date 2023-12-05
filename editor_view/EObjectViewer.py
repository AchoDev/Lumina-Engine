import pygame
from .collidepoint import collidepoint
from .EditorComponent import EditorComponent
from .EText import EText

class EObjectViewer(EditorComponent):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.height = 300
        self.onclick = None

        self.buttons = []

    def get_height(self):
        return self.height

    def update(self, mouse_event):
        if(self.scene == None): return
        if(self.buttons == []):
            self.buttons = [EObjectButton(obj.__class__.__name__, lambda: self.onclick(obj)) for obj in self.scene.objects]

        # if(len(self.buttons) != len(self.scene.objects)):
        #     for obj in self.scene.objects[ len(self.scene.objects) - len(self.buttons) : len(self.scene.objects) ]:
        #         self.buttons.append(EObjectButton(obj.__class__.__name__, lambda: self.onclick(obj)))

        for button in self.buttons:
            button.update(mouse_event)

    def get_surface(self, editor_width):
        back = pygame.Surface((editor_width, self.get_height()), pygame.SRCALPHA)

        current_y = 0
        for button in self.buttons:
            back.blit(button.get_surface(editor_width), (0, current_y))
            
            button.y = current_y + self.y

            current_y += button.get_height()
            current_y += 4

        return back

class EObjectButton(EditorComponent):
    def __init__(self, name, onclick):
        super().__init__()
        self.width = 0
        self.height = 20
        self.name = name
        self.onclick = onclick

        self.hovered = False
        self.clicked = False
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def update(self, mouse_event):
        mouse_pos = pygame.mouse.get_pos()
    
        if(pygame.mouse.get_pressed()[0]):
            if(self.hovered and not self.clicked):
                self.onclick()
                self.clicked = True
        else:
            self.clicked = False
            if(collidepoint(mouse_pos, (self.x, self.y, self.width, self.height))):
                self.hovered = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                mouse_event.value = self
            else:
                self.hovered = False
                if(mouse_event.value == self):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    def get_surface(self, editor_width):
        self.width = editor_width

        back = pygame.Surface((editor_width, self.height), pygame.SRCALPHA)
        back.fill(self.dark_gray)
        text = EText(self.name, 14)
        back.blit(text.get_surface(editor_width), (25, self.height / 2 - text.get_height() / 2))
        
        return back
    

