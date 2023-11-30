class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def normalize(self):
        pass

    def to_tuple(self):
        return (self.x, self.y)

    def reset(self):
        self.x, self.y = 0

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
    

    