
from __init__ import * # LUMINA ENGINE IMPORT

init((800, 800))

scene = Scene('main screen')
scene.fill(light_blue)

box = scene.add_object(Square(0, 0, 1, 1, blue))

while True:
    scene.load()

    if(get_key("up")): scene.camera.transform.y += 0.01
    if(get_key("down")): scene.camera.transform.y -= 0.01
    if(get_key("right")): scene.camera.transform.x -= 0.01
    if(get_key("left")): scene.camera.transform.x += 0.01



