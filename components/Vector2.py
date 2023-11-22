class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def normalize(self):
        pass

    def reset(self):
        self.x, self.y = 0

    def __repr__(self) -> str:
        return f'Vector2({self.x}, {self.y})'

    @classmethod
    def from_tuple(cls, tuple):
        return cls(tuple[0], tuple[1])

    