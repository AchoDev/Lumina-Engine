import math
from pygame import Vector2, Rect, Surface
from pygame.transform import scale

def calculate_distance(deg):
    
    def sin(num):
        return math.sin(num * (math.pi / 180))
    
    def cos(num):
        return math.cos(num * (math.pi / 180))

    def square(num):
        return num**2

    def direction():
        return Vector2(cos(deg), sin(deg))

    def r_variable():
        return (-20 * sin(deg) + math.sqrt(square(20) * square(sin(deg)) - 4 * square(cos(deg)) * (-100))) / (2 * square(cos(deg)))

    def cross_point():
        return Vector2(r_variable() * direction().x,  r_variable() * direction().y)


    return cross_point().length()

def crop(s, x, y, w, h):
    rect = Rect(x, y, w, h)
    cropped = Surface(rect.size)
    cropped.blit(s, (0, 0), rect)

    return cropped

def warp_surface(screen_width, surface, start, end):
    surface_list = []

    clamp = (start, 180 - end)
    for i in range(screen_width - clamp[0] - clamp[1]):

        slice_height = surface.get_size()[1]
        degree = (start + end) * (i / screen_width)
        slice = crop(surface, start + i, 0, 1, slice_height)
        surface_list.append(scale(slice, (1, slice_height * (calculate_distance(degree)) / 4)))
        # surface_list.append(slice)

    return surface_list