from __init__ import *

window_dim = (1000, 800)
init(window_dim)

scene = Scene("t")
scene.fill(light_blue)

b = scene.add_object(Square(-5.1, 0, 1, 1, green))
b.add_component(Rigidbody())
b.add_component(Boxcollider())

# b2 = scene.add_object(Square(0, 1, 1, 1, red))
# b2.add_component(Rigidbody())
# b2.add_component(Boxcollider())

b3 = scene.add_object(Square(0, 3, 10, 1, violet))
b3.add_component(Boxcollider())


scene.camera.transform.x = 10



while True:
    mouse_pos = scene.camera.window_to_world_position(get_mouse_pos())

    if(get_key('a')):
        new = scene.add_object(Square(mouse_pos.x, mouse_pos.y, 0.5, 0.5, white))
        new.add_component(Rigidbody())
        new.add_component(Boxcollider())

    scene.load()

    pass

