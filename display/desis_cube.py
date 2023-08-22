import pygame
from .constances import CITY_RADIUS
from .color import colors_palet
from .Color import Color

def draw_desis_cube(screen, city):
    colors = list(Color)
    for desis_type, number_of_cube in enumerate(city.disease_cubes):
        for cube_cunter in range(number_of_cube):
            desis_point = positions(city.point, desis_type, cube_cunter)     
            draw_squer(screen, desis_point, colors[desis_type].name)

def positions(point, desis_type, cube_cunter):
    LENTH_BETWEEN_CUBES = 15
    LENTH_MOD_FROM_CENTER = 1.7
    move_aside = CITY_RADIUS * LENTH_MOD_FROM_CENTER
    move_from_center = (cube_cunter - 1) * LENTH_BETWEEN_CUBES
    positions = [(point[0] - move_from_center, point[1] + move_aside),
                 (point[0] + move_aside, point[1] - move_from_center), 
                 (point[0] - move_from_center, point[1] - move_aside), 
                 (point[0] - move_aside, point[1] - move_from_center)]
    return positions[desis_type]

def draw_squer(screen, point, color):
    HALF_HIGHT = 0.15 * CITY_RADIUS
    a,b,c,d = point[0] + HALF_HIGHT, point[1] + HALF_HIGHT, point[1] - HALF_HIGHT, point[0] - HALF_HIGHT
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet[color], points=rectangle_point)







