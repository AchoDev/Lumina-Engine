
import pygame, console, delta_time
from main import WIN

class Eventloop:
    def __init__(self, physics_world, events=[]):
        self.running = False
        self.events = events
        self.world = physics_world

    def add_event(self, event):
        self.events.append(event)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            for custom_event in self.events:
                if event.type == custom_event.get_event():
                    custom_event.hit(event)

            if event.type == pygame.VIDEORESIZE:
                WIN.videoresize()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    console.is_visible = not console.is_visible

                for custom_event in self.events:
                    if custom_event.type == "keyevent" and event.key == custom_event.event:
                        custom_event.hit()
                        


        delta_time.update_delta_time()
        console.draw_console()
        self.world.Step(1.0 / 60, 6, 2)
        self.world.ClearForces()

        pygame.display.update()

