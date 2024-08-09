from typing import Any
from __init__ import *
from enum import Enum

window_dim = (1000, 600)
init(window_dim)

scene = Scene("t")
scene.fill(light_blue)

class DragAround(Component):
    def __init__(self):
        super().__init__()
        self.dragging = False
    
    def initialize(self):
        self.rb: Rigidbody = self.target.get_component("Rigidbody")   
    
    def update(self, scene):
        if not get_mouse()[0]: 
            self.dragging = False
            self.rb.velocity = Vector2(0, 0)
            return

        if check_collision_point(self.target, scene.mouse_to_world().to_tuple()) or self.dragging:
            self.rb.smooth_move_to(scene.mouse_to_world(), 30)
            self.dragging = True


b = scene.add_object(Square(1, 0, 4, 1, green))
b.add_component(Rigidbody(static=True))
b.add_component(Boxcollider())
b.add_component(DragAround())

b2 = scene.add_object(Square(0, 1, 1, 4, red))
b2.add_component(Rigidbody(static=True))
b2.add_component(Boxcollider())
b.add_component(DragAround())

b3 = scene.add_object(Square(0, 3, 10, 1, violet))
b3.add_component(Boxcollider())

# b4 = scene.add_object(Square(0, 0, 10, 1, orange))
# b4.transform.angle = 45
# b4.add_component(Rigidbody(static=True))
# b4.add_component(Boxcollider())
# b4.add_component(DragAround())

canvas = scene.add_object(Canvas())

console.watch(lambda: b.transform.position.rounded(), "b pos")
console.watch(lambda: scene.mouse_to_world().rounded(), "mtw")

while True:
    mouse_pos = scene.camera.window_to_world_position(get_mouse_pos())

    if(get_key('a')):
        new = scene.add_object(Square(mouse_pos.x, mouse_pos.y, 0.5, 0.5, white))
        new.add_component(Rigidbody())
        new.add_component(Boxcollider())

    # debug_cube.transform.set_position(mouse_pos)

    scene.load()

    pass

