

class Event:
    def __init__(self, pygame_event, event_handler):
        self.event = pygame_event
        self.event_handler = event_handler

        self.type = "event"

    def get_event(self):
        return self.event

    def hit(self):
        self.event_handler()

    