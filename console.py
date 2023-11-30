
from cls import *
from main import WIN
from components.Transform import Transform
import asyncio, delta_time

__print_list = []
__watch_list_c = [] # c -> container
__watch_list = []
max_log_count = 100

def log(string):

    __print_list.insert(0, string)

    # def remove_entry():
    #     __print_list.remove(string)

    # if len(__print_list) < max_log_count:
    #     asyncio.create_task(__remove_log(remove_entry))
    # else:
    #     __print_list.pop(0)
        
async def __remove_log(function):
    await asyncio.sleep(3)
    function()

console_size = (350, 400)
console_pos = (1920 - console_size[0], 1080 - console_size[1])

__ct = Transform(*console_pos, *console_size)
font_size = 18
text_height = 20
font = 'lucidaconsole'

is_visible = False

def watch(variable, name):
    __watch_list.insert(0, (variable, name))

watch(lambda: round(delta_time.get_average_fps(), 2), 'fps')

def draw_console():

    if is_visible:
        __ct.x = WIN.width - console_size[0]
        __ct.y = WIN.height - console_size[1]

        __ct2 = __ct.copy_with(
            y= __ct.y - 205,
            height=200,
        )

        WIN.draw_transparent_square(__ct, Colors.black, 128)
        WIN.draw_transparent_square(__ct2, Colors.black, 128)
        
        WIN.draw_text('watch', Colors.lavender, __ct2.position.to_tuple(), 27, font, )
        WIN.draw_text('console', Colors.lavender, __ct.position.to_tuple(), 27, font, )

        i = text_height
        for variable in __watch_list[::-1]:
            WIN.draw_text(variable[1] + ': ' + str(variable[0]()), Colors.white, (__ct.x + 10, __ct2.y + i + 20), font_size, font)
            i += text_height        

        i = text_height
        for log in __print_list:
            if i < __ct.height:
                WIN.draw_text(log, Colors.white, (__ct.x + 10, __ct.y + i + 20), font_size, font)
            i += text_height
