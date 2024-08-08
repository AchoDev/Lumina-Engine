from __init__ import *
from enum import Enum

window_dim = (1000, 600)
init(window_dim)

scene = Scene("t")
scene.fill(light_blue)

b = scene.add_object(Square(1, 0, 1, 1, green))
# b.add_component(Rigidbody())
b.add_component(Boxcollider())

# b2 = scene.add_object(Square(0, 1, 1, 1, red))
# b2.add_component(Rigidbody())
# b2.add_component(Boxcollider())

# b3 = scene.add_object(Square(0, 3, 10, 1, violet))
# b3.add_component(Boxcollider())

# debug_cube = scene.add_object(Square(0, 0, 1, 1, orchid))
# debug_cube.name = 'DEBUG CUBE'

# scene.camera.transform.x = 10

show_box = Container(False)
move_box = Container(False)

console.watch(lambda: scene.camera.transform.get_position().x, 'camX')
console.watch(lambda: scene.camera.transform.get_position().y, 'camY')
console.watch(lambda: scene.camera.transform.get_size(), 'camSize')
console.watch(lambda: scene.camera.orthographic_size, 'orthoSize')

scene.add_event(KeyEvent('h', lambda: console.log('hello achodev.me!')))
scene.add_event(KeyEvent('q', lambda: show_box.toggle()))
scene.add_event(KeyEvent('w', lambda: move_box.toggle()))

while True:
    mouse_pos = scene.camera.window_to_world_position(get_mouse_pos())

    if(get_key('a')):
        new = scene.add_object(Square(mouse_pos.x, mouse_pos.y, 0.5, 0.5, white))
        new.add_component(Rigidbody())
        new.add_component(Boxcollider())

    if show_box.value:
        b.active = True
        if move_box.value:
            b.transform.set_position(mouse_pos)
    else:
        b.active = False

    # debug_cube.transform.set_position(mouse_pos)

    scene.load()

    pass

