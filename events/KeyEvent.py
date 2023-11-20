
from .Event import Event

class KeyEvent(Event):
    def __init__(self, key_pressed, event_handler=None):
        super().__init__(key_pressed, event_handler)

        self.type = "keyevent"