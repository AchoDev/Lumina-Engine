from __init__ import *

window_dim = (750, 800)
init(window_dim)

scene = Scene("t")
scene.fill("white")

b = scene.add_object(Square(1, 1, 1, 1, blue))
b.add_component(Rigidbody(b, False))

b2 = scene.add_object(Square(0, 10, 10, 1, black))
b2.add_component(Rigidbody(b2, True))


# scale_up = scene.add_event(KeyEvent("e"))
# scale_down = scene.add_event(KeyEvent("r"))

# movement_events = [
#     scene.add_event(KeyEvent("left")),
#     scene.add_event(KeyEvent("right")),
#     scene.add_event(KeyEvent("up")),
#     scene.add_event(KeyEvent("down")),
# ]

console.watch(b2.transform, "", True)

camera = scene.camera

while True:
    
    # if(scale_up.check()): scene.camera.orthographic_size += 0.1
    # if(scale_down.check()): scene.camera.orthographic_size -= 0.1

    # if(movement_events[0].check()): scene.camera.transform.x += 0.1
    # if(movement_events[1].check()): scene.camera.transform.x -= 0.1
    
    # if(movement_events[2].check()): scene.camera.transform.y += 0.1
    # if(movement_events[3].check()): scene.camera.transform.y -= 0.1

    if(get_key('right')): 
        scene.camera.transform.x -= 5 * delta_time.DELTA_TIME
    if(get_key('left')): 
        scene.camera.transform.x += 5 * delta_time.DELTA_TIME
    if(get_key('up')): 
        scene.camera.transform.y += 5 * delta_time.DELTA_TIME
    if(get_key('down')): 
        scene.camera.transform.y -= 5 * delta_time.DELTA_TIME

    if(get_key('e')):
        scene.camera.orthographic_size *= 0.99
    if(get_key('r')):
        scene.camera.orthographic_size /= 0.99

    print(scene.camera.orthographic_size)

    scene.load()


