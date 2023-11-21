from __init__ import *

window_dim = (750, 800)
init(window_dim)

scene = Scene("t")
scene.fill(light_blue)

b = scene.add_object(Square(-50, -2.5, 1, 1, blue))
b.add_component(Rigidbody(b, False))

b3 = scene.add_object(Square(1.5, -1, 1, 1, blue))
b3.add_component(Rigidbody(b3, False))

b2 = scene.add_object(Square(0, 1, 10, 1, red))
b2.add_component(Rigidbody(b2, True))

ground = [
    Square(-5, 5, 1, 10, red),
    Square(5, 5, 1, 10, red),
    Square(0, 10, 40, 1, red),
]

for g in ground:
    g.add_component(Rigidbody(g, True))

scene.add_multiple_objects(ground)


mouse_collider = scene.add_object(Square(0, 0, 0.5, 0.5, orange))
mouse_collider.add_component(Rigidbody(mouse_collider, False))

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

b2rb: Rigidbody = b.get_component("Rigidbody")
b2rb.move_position(Vector2(1, 1))

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
        # rb: Rigidbody = b2.get_component("Rigidbody")
        # rb.add_force(10)

        # b3.add_component(Rigidbody(b3, False))

        # b.add_component(Rigidbody(b, False))

        new_instance = scene.add_object(Square(0, -3, 1, 1, white))
        new_instance.add_component(Rigidbody(new_instance, False))

    mouse_pos = scene.camera.window_to_world_position(get_mouse_pos())

    rb = mouse_collider.get_component("Rigidbody")
    rb.move_position(scene.camera.window_to_world_position(get_mouse_pos()))
    # print(mouse_collider.transform.get_position())

    # if(b2rb.b2box != None): print(b2rb.b2box.linearVelocity)
    

    scene.load()


