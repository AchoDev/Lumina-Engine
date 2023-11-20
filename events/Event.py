

class Event:
    def __init__(self, pygame_event, event_handler = None):
        self.event = pygame_event
        self.event_handler = event_handler

        self.isHit = False

        self.type = "event"

    def get_event(self):
        return self.event

    def hit(self):
        self.isHit = True

        if(self.event_handler != None):
            self.event_handler()

    def check(self):
        return self.isHit

    

    