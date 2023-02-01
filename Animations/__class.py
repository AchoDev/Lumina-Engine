
import main, enum

def square(value):
    return value * value

def cube(value):
    return value * value * value

def raise__to_the_power_of(value, power):
    first_value = value
    for i in range(power - 1):
        value *= first_value    
    return value

def lerp(start, end, pct):
    return (start + (end - start) * pct)

def ease_in(pct):
    return raise__to_the_power_of(pct, 5)

def flip(x):
    return 1 - x

def ease_out(pct):
    return flip(raise__to_the_power_of(flip(pct), 5))

def ease_in_out(pct):
    return lerp(ease_in(pct), ease_out(pct), pct)

class Animation:
    # TYPES --> 1: linear, 2: ease-in, 3: ease-out, 4: ease-in-out

    pct = 0
    is_finished = False

    def __init__(self, target, start_point, end_point, type, duration, event, args = None):
        self.target = target
        self.start = start_point
        self.end = end_point
        self.type = type

        self.duration = duration
        self.time = 0

        self.event = event
        self.args = args

    def update(self, dt):
        self.pct += 0.1 #self.speed
        value = None
        match self.type:
            case 1:
                pct = (self.time / self.duration)
            case 2:
                pct = ease_in(self.time / self.duration)
            case 3:
                pct = ease_out(self.time / self.duration)
            case 4:
                pct = ease_in_out(self.time / self.duration)
        
        distance = (abs(lerp(self.start[0], self.end[0], pct)), abs(lerp(self.start[1], self.end[1], pct)))
    
        self.target.x = distance[0]
        self.target.y = distance[1]

        if self.time <= self.duration:
            self.time += (1 / (1 / dt))
        else:
            self.is_finished = True

            if self.event != None:
                if self.args != None:
                    self.event(*self.args)
                else:
                    self.event()

        # print(round(distance, 5), "- - -", round(dt, 5), "- - -", abs(self.target.x - value))
        # print(self.time, self.duration, round(self.time / self.duration, 2), "FPS:", 1 / dt)
        # self.target.y = value[1]

        # print(distance)
        # print(self.start)
        # print(self.end)
        # print()


class Animation_Type(enum.Enum):
    linear = 1
    ease__in = 2
    ease__out = 3
    ease__in__out = 4
    

