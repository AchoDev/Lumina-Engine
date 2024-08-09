from __init__ import *
from enum import Enum

window_dim = (1000, 600)
init(window_dim)

scene = Scene("t")
scene.fill(light_blue)

b = scene.add_object(Square(1, 0, 4, 1, green))
b.add_component(Rigidbody(static=True))
b.add_component(Boxcollider())

b2 = scene.add_object(Square(0, 1, 1, 4, red))
b2.add_component(Rigidbody(static=True))
b2.add_component(Boxcollider())

b3 = scene.add_object(Square(0, 3, 10, 1, violet))
b3.add_component(Boxcollider())


bucket1 = scene.add_object(Square(0, 1, 5, 1, blue_violet))
bucket1.add_component(Rigidbody(static=True))
bucket1.add_component(Boxcollider())

bucket2 = scene.add_object(Square(0, 1, 1, 4, blue_violet))
bucket2.add_component(Rigidbody(static=True))
bucket2.add_component(Boxcollider())

bucket3 = scene.add_object(Square(0, 1, 1, 4, blue_violet))
bucket3.add_component(Rigidbody(static=True))
bucket3.add_component(Boxcollider())

canvas = scene.add_object(Canvas())
platform_indicator = canvas.add_child(Text(0, 0, 'Platform', 20, white))

# debug_cube = scene.add_object(Square(0, 0, 1, 1, orchid))
# debug_cube.name = 'DEBUG CUBE'

# scene.camera.transform.x = 10

class BoxType(Enum):
    NONE = 0
    PLATFORM = 1
    WALL = 2
    BUCKET = 3

current_box = Container(BoxType.NONE)

def switch_box():

    current_box.value = BoxType((current_box.value.value + 1) % 4) 

console.watch(lambda: scene.mouse_to_window(), 'mtw')

scene.add_event(KeyEvent('q', lambda: switch_box()))

while True:
    mouse_pos = scene.camera.window_to_world_position(get_mouse_pos())

    if(get_key('a')):
        new = scene.add_object(Square(mouse_pos.x, mouse_pos.y + 3, 0.5, 0.5, white))
        new.add_component(Rigidbody())
        new.add_component(Boxcollider())


    speed = 30

    b.get_component("Rigidbody").velocity = Vector2(0, 0)
    b2.get_component("Rigidbody").velocity = Vector2(0, 0)
    bucket1.get_component("Rigidbody").velocity = Vector2(0, 0)
    bucket2.get_component("Rigidbody").velocity = Vector2(0, 0)
    bucket3.get_component("Rigidbody").velocity = Vector2(0, 0)


    match current_box.value:
        case BoxType.PLATFORM:
            b.get_component("Rigidbody").smooth_move_to(mouse_pos, speed)
        case BoxType.WALL:
            b2.get_component("Rigidbody").smooth_move_to(mouse_pos, speed)
        case BoxType.BUCKET:
            bucket1.get_component("Rigidbody").smooth_move_to(mouse_pos, speed)
            bucket2.get_component("Rigidbody").smooth_move_to(mouse_pos + Vector2(2, - 2), speed)
            bucket3.get_component("Rigidbody").smooth_move_to(mouse_pos + Vector2(-2, - 2), speed)


    # debug_cube.transform.set_position(mouse_pos)

    scene.load()

    pass

