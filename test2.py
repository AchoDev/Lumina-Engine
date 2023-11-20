from __init__ import *

window_dim = (750, 800)
init(window_dim)

scene = Scene("t")
scene.fill("white")

b = scene.add_object(Square(1, 1, 1, 1, blue))
b.add_component(Rigidbody(b, False))

b2 = scene.add_object(Square(0, 10, 10, 1, red))
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
    
    def print_info():
        print(scene.camera.orthographic_size)
        print(scene.camera.transform.get_position())
        print(b2.transform.get_position())

        print("")

    if(get_key('right')): 
        scene.camera.transform.x -= 20 * delta_time.DELTA_TIME * (scene.camera.orthographic_size / 20)
        print_info()
    
    if(get_key('left')): 
        scene.camera.transform.x += 20 * delta_time.DELTA_TIME * (scene.camera.orthographic_size / 20)
        print_info()
    
    if(get_key('up')): 
        scene.camera.transform.y += 20 * delta_time.DELTA_TIME * (scene.camera.orthographic_size / 20)
        print_info()
    
    if(get_key('down')): 
        scene.camera.transform.y -= 20 * delta_time.DELTA_TIME * (scene.camera.orthographic_size / 20)
        print_info()

    if(get_key('e')):
        scene.camera.orthographic_size *= 0.99
        print_info()
        

    if(get_key('r')):
        scene.camera.orthographic_size /= 0.99
        print_info()
    

    if(get_key('a')):
        rb: Rigidbody = b2.get_component("Rigidbody")
        rb.add_force(10)

    scene.load()


