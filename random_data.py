import random
import math

def get_circle_random_points(center, R, n):
    points = []
    for i in range(n):
        theta = random.uniform(0.0, 360.0)
        r = math.sqrt(random.random()) * R
        points.append((r * math.sin(theta) + center[0], r * math.cos(theta) + center[1]))
    return points

def get_box_random_points(leftbottom, upperright, n):
    points = []
    for i in range(n):
        x = random.uniform(leftbottom[0], upperright[0])
        y = random.uniform(leftbottom[1], upperright[1])
        points.append((x, y))
    return points

