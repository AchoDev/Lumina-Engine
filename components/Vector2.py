

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def normalize(self):
        pass

    def to_tuple(self):
        return (self.x, self.y)

    def to_transform(self):
        from .Transform import Transform
        return Transform(self.x, self.y, self.x, self.y)

    def reset(self):
        self.x, self.y = 0

    def rounded(self):
        return self.copy_with(round(self.x, 2), round(self.y, 2))

    def copy_with(self, x=None, y=None):
        return Vector2(
            self.x if x == None else x,
            self.y if y == None else y
        )

    def __repr__(self) -> str:
        return f'Vector2({self.x}, {self.y})'

    def __add__(self, other):
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def __sub__(self, other):
        return Vector2(
            self.x - other.x,
            self.y - other.y
        )
    
    def __truediv__(self, other):
        return Vector2(
            self.x / other,
            self.y / other
        )
    
    def __mul__(self, other):
        if(type(other) == 'Vector2'):
            return Vector2(
                self.x * other.x,
                self.y * other.y
            )
        else:
            return Vector2(
                self.x * other,
                self.y * other
            )
        
    @classmethod
    def from_tuple(cls, tuple):
        return cls(tuple[0], tuple[1])
    

    