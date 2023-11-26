
from .Component import Component

from Box2D import b2FixtureDef, b2PolygonShape

class Boxcollider(Component):
    def __init__(self, size=None):
        super().__init__()
        self.size = size
        self.fixture = None

    def initialize(self):
        if(self.size == None):
            self.size = (self.target.transform.get_size() / 2).to_tuple()

        self.fixture = self.target.b2Body.CreateFixture(
            b2FixtureDef(
                shape=b2PolygonShape(
                    box=self.size
                )
            )
        )

        print("")