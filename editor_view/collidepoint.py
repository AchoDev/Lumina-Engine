
def collidepoint(point, area) -> bool:
    return (point[0] > area[0] and point[0] < area[0] + area[2]) and (point[1] > area[1] and point[1] < area[1] + area[3])