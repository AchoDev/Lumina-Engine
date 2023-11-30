
import pygame, console, delta_time
from main import WIN
from Input import current_mouse_wheel_scroll

class Eventloop:
    def __init__(self, physics_world, events=[]):
        self.running = False
        self.events = events
        self.world = physics_world

    def add_event(self, event):
        self.events.append(event)

    def update(self):

        scrolling_hit = False

        custom_event_hits = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            for custom_event in self.events:
                if event.type == custom_event.get_event():
                    custom_event.hit(event)
                    custom_event_hits.append(custom_event)

            if event.type == pygame.VIDEORESIZE:
                WIN.videoresize()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    console.is_visible = not console.is_visible

                for custom_event in self.events:
                    if custom_event.type == "keyevent":
                        if( 
                            (event.unicode == custom_event.event) or
                            (custom_event.event == 'left' and event.key == pygame.K_LEFT) or 
                            (custom_event.event == 'right' and event.key == pygame.K_RIGHT) or 
                            (custom_event.event == 'up' and event.key == pygame.K_UP) or 
                            (custom_event.event == 'down' and event.key == pygame.K_DOWN)):
                                custom_event.hit()
                                custom_event_hits.append(custom_event)
                        
            if event.type == pygame.MOUSEWHEEL: 
                scrolling_hit = True
                current_mouse_wheel_scroll.x = event.x
                current_mouse_wheel_scroll.y = event.y

        for custom_event in self.events:
            if not (custom_event in custom_event_hits):
                custom_event.isHit = False


        if(not scrolling_hit): 
            current_mouse_wheel_scroll.x = 0
            current_mouse_wheel_scroll.y = 0 

        delta_time.update_delta_time()
        console.draw_console()
        self.world.Step(delta_time.DELTA_TIME, 10, 10)
        self.world.ClearForces()

        pygame.display.update()

