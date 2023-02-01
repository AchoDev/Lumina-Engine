import time
from cls.Container import Container

DELTA_TIME = 0
prev_time = time.time()

count = 600
__fps_list = [30]
average_fps = 0
afc = Container(0)

def update_delta_time():
    global prev_time, DELTA_TIME, average_fps
    now = time.time()
    DELTA_TIME = now - prev_time
    prev_time = now

    afc.value = round(average_fps, 2)

    __fps_list.append(get_fps())

    if len(__fps_list) == count:
        average_fps = get_average_fps()
        __fps_list.clear()
        __fps_list.append(average_fps)


def get_fps():
    return 0 if DELTA_TIME == 0 else 1 / DELTA_TIME

def get_average_fps():
    fps = 0

    for num in __fps_list:
        fps += num

    fps /= len(__fps_list)

    return fps