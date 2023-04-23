import os
from __init__ import *
from testproj.perspective import warp_surface

window_size = (1350, 1080)
init(window_size)

main_menu = Scene("main-menu")
main_menu.fill(white)

sqr = Square(10, 10, 100, 100, blue)
main_menu.add_one(sqr)

original_background = Image()
original_background.set_image("./office2.jpg")

background = Image()
background.set_image("./office2.jpg")
background.resize(1920, 1080)


# background = Surface(100, 100, crop(background.image, 100, 100, 200, 300))
# main_menu.add_one(background)

middle = 90
fov = 1

list_container = GameObject(0, 0, 1920, 1080)
main_menu.add_one(list_container)

def generate_image():
    background.image = original_background.image
    list = warp_surface(1920, background.image, middle + fov // 2, middle - fov // 2)

    list_container.clear_children()
    print(len(list))
    for i in range(1920):
        index = int(i * (len(list) / 1920))
        list_container.add_child(Surface(i, (1080 - list[index].get_size()[1]) // 2, list[index]))

# main_menu.add_one(Surface(10, 10, list))

generate_image()
    

# sqr.add_component(Rigidbody.Rigidbody(sqr))


def turn(val):
    global middle
    middle += val

    generate_image()



main_menu.add_event(KeyEvent(pygame.K_LEFT, lambda: turn(-1)))
main_menu.add_event(KeyEvent(pygame.K_RIGHT, lambda: turn(1)))

def reset_pos():
    sqr.set_y(0)
    sqr.get_component("Rigidbody").yVel = 0
    console.log("POSITION RESET")

add_force_event = KeyEvent(pygame.K_c, lambda: sqr.get_component("Rigidbody").add_force(500))
reset_event = KeyEvent(pygame.K_x, reset_pos)

main_menu.add_many_events([add_force_event, reset_event])

rb = sqr.get_component("Rigidbody")

fps = Container(0)

console.watch(fps, "fps", True)



while True:
    if(pygame.mouse.get_pos()[0] > 1000):
        turn(1)
    elif(pygame.mouse.get_pos()[0] < 300):
        turn(-1)

    
    main_menu.load()
    fps.change(round(delta_time.get_average_fps(), 2))