
from cls import *
from main import WIN
from components.Transform import Transform

__print_list = []
__watch_list_c = [] # c -> container
__watch_list = []
max_log_count = 100

def log(string):

    __print_list.insert(0, string)

    def remove_entry():
        __print_list.remove(string)

    if len(__print_list) < max_log_count:
        wait_and_call(3, remove_entry)
    else:
        __print_list.pop(0)
        

console_size = (400, 500)
console_pos = (1920 - console_size[0], 1080 - console_size[1])

__ct = Transform(*console_pos, *console_size)
font_size = 50
text_height = 35

is_visible = False

def watch(variable, name, is_obj=False):
    if is_obj:
        __watch_list_c.insert(0, (variable, name))
    else:
        __watch_list.insert(0, (variable, name))


def draw_console():

    if is_visible:
        WIN.draw_transparent_square(__ct, Colors.black, 128)
        
        i = text_height
        for variable in __watch_list:
            WIN.draw_one(Text(__ct.x, (1080 - __ct.height) + i , font_size, Colors.white, variable[1] + ": " + str(variable[0])), 1920)
            i += text_height

        for variable in __watch_list_c:
            WIN.draw_one(Text(__ct.x, (1080 - __ct.height) + i , font_size, Colors.white, variable[1] + ": " + str(variable.repr())), 1920)
            i += text_height

        i = text_height
        for log in __print_list:
            if i < __ct.height:
                WIN.draw_one(Text(__ct.x, 1080 - i, font_size, Colors.white, log), 1920)
            i += text_height
