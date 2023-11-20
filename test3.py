
from __init__ import * # LUMINA ENGINE IMPORT

init((800, 800))

scene = Scene('main screen')

box = scene.add_object(Square(0, 0, 1, 1, blue))
box.add_component(Rigidbody(box, False))

# BOX2d physics support
# DOESNT WORK RIGHT NOW :(

ground = scene.add_object(Square(0, -1, 5, 1, red))
ground.add_component(Rigidbody(ground, True))

while True:
    scene.load()

    if(get_key("up")): scene.camera.transform.y += 0.01
    if(get_key("down")): scene.camera.transform.y -= 0.01
    if(get_key("right")): scene.camera.transform.x -= 0.01
    if(get_key("left")): scene.camera.transform.x += 0.01



