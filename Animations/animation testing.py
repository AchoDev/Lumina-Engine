import pygame

background_color = (255,255,255)

(width, height) = (450, 450)

screen = pygame.display.set_mode((width, height))

screen.fill(background_color)

def lerp(start, end, pct):
    return (start + (end - start) * pct)

def ease_in(pct):
    return pct * pct

def flip(x):
    return 1 - x

def ease_out(pct):
    return flip(flip(pct) * flip(pct))

def ease_in_out(pct):
    return lerp(ease_in(pct), ease_out(pct), pct)

percentage = 0
x = 10
pct = 0
running = True

start = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, 195, 30, 30))


    x = lerp(0, 200, ease_in_out(pct))



    if pct <= 1:
        pct += 0.01

        

    pygame.display.update()





# def ease_in(start, end)