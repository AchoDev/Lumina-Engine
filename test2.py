from __init__ import *

window_dim = (750, 800)
init(window_dim)

scene = Scene("t")
scene.fill("white")

b = scene.add_one(Square(10, 10, 50, 50, blue))
b.add_component(Rigidbody(b, False))

b2 = scene.add_one(Square(0, 600, 1000, 50, black))
b2.add_component(Rigidbody(b2, True))

def change_y():
    b2.transform.y += 10

scene.add_event(KeyEvent("e", change_y()))

console.watch(b2.transform, "", True)


while True:
    print(b2.transform.y)
    scene.load()


