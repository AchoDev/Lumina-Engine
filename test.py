from __init__ import *

init((1350, 1080))

main_menu = Scene("main-menu")
main_menu.fill(white)

sqr = Square(10, 10, 100, 100, blue)
main_menu.add_one(sqr)

# sqr.add_component(Rigidbody.Rigidbody(sqr))

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
    main_menu.load()
    fps.change(round(delta_time.get_average_fps(), 2))