from __init__ import *

window_dim = (1000, 800)
init(window_dim)

scene = Scene("t")
scene.fill(light_blue)

b = scene.add_object(Square(-50, -2.5, 1, 1, blue))
b.add_component(Rigidbody(False))

b3 = scene.add_object(Square(1.5, -1, 1, 1, blue))
b3.add_component(Rigidbody(False))

b2 = scene.add_object(Square(0, 1, 10, 1, red))
b2.add_component(Rigidbody(True))

scene.camera.transform.y = 0

ground = [
    # Square(-5, 5, 1, 10, red),
    # Square(5, 5, 1, 10, red),
    Square(0, 0, 1, 7, green),
    Square(0, 10, 40, 1, red),
    Square(-20, 0, 1, 40, red),
    Square(20, 0, 1, 40, red),

    Square(50, 50, 1, 1, violet),
]

for g in ground:
    g.add_component(Rigidbody(True))

scene.add_multiple_objects(ground)


mouse_collider = scene.add_object(GameObject(0, 0, 0, 0))

mouse_collider.add_child(Square(0, 0, 5, 0.5, orange)).add_component(Rigidbody(False)).fixed_rotation = False
mouse_collider.add_child(Square(-4.5, 0, 0.5, 1, orange)).add_component(Rigidbody(False)).fixed_rotation = False

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
    
    mouse_pos = scene.camera.window_to_world_position(get_mouse_pos())

    if(get_key('a')):
        # rb: Rigidbody = b2.get_component("Rigidbody")
        # rb.add_force(10)

        # b3.add_component(Rigidbody(b3, False))

        # b.add_component(Rigidbody(b, False))

        scene.add_object(Square(mouse_pos.x, mouse_pos.y - 1, 0.1, 0.1, white)).add_component(Rigidbody(False))        


    # rb: Rigidbody = mouse_collider.get_component("Rigidbody")
    # rb.move_position(scene.camera.window_to_world_position(get_mouse_pos()))
    # print(rb.velocity)

    mouse_collider.transform.set_position(mouse_pos)


    scene.load()


