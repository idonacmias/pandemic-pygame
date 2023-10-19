import pygame

from .color import colors_palet
from .constances import CITY_RADIUS, EDGE_CITIES, RESEARCH_STATION_RADIUS
from .Color import Color



def draw(city, screen, font):
    color = colors_palet[city.color.name]
    city.rect = pygame.draw.circle(surface=screen, color=color, center=city.point , radius=CITY_RADIUS)
    if city.research_station:
        pygame.draw.circle(surface=screen, color=colors_palet['WHITE'], center=city.rect.center , radius=RESEARCH_STATION_RADIUS)

    font_point = (city.point[0] - 5 * len(city.name), city.point[1] + 20)        
    text_surface = font.render(city.name, True, colors_palet['WHITE']) 
    screen.blit(text_surface, font_point)
    draw_diseasse_cubes(screen, city)


def draw_diseasse_cubes(screen, city):
    for color in list(Color):
        for cube_cunter in range(city.diseasse_cubes[color.name]):
            desis_point = desis_positions(city.point, color, cube_cunter)     
            draw_squer(screen, desis_point, color.name)


def desis_positions(point, color, cube_cunter):
    LENTH_BETWEEN_CUBES = 15
    LENTH_MOD_FROM_CENTER = 1.7
    move_aside = CITY_RADIUS * LENTH_MOD_FROM_CENTER
    move_from_center = (cube_cunter - 1) * LENTH_BETWEEN_CUBES
    positions = {'BLUE' : (point[0] - move_from_center, point[1] + move_aside),
                 'BLACK' : (point[0] + move_aside, point[1] - move_from_center), 
                 'YELLOW' : (point[0] - move_from_center, point[1] - move_aside), 
                 'RED' : (point[0] - move_aside, point[1] - move_from_center)}
    return positions[color.name]


def draw_squer(screen, point, color):
    HALF_HIGHT = 0.15 * CITY_RADIUS
    a,b,c,d = point[0] + HALF_HIGHT, point[1] + HALF_HIGHT, point[1] - HALF_HIGHT, point[0] - HALF_HIGHT
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet[color], points=rectangle_point)


def conect_routes(city, screen, cities, font):
    for other_city_name in city.routes:
        other_city = cities[other_city_name]
        if is_edge_conection(city, other_city):
            conect_to_shadow_point(screen, font, city, other_city)

        else:
            pygame.draw.line(screen, colors_palet['PINK'], city.point, other_city.point, 2)


def is_edge_conection(city, other_city):
    return city.name in EDGE_CITIES and abs(other_city.point[0] - city.point[0]) > 500


def conect_to_shadow_point(screen, font, city, other_city):
    shadow_point = clculate_shadow_point(city.point, other_city.point)
    pygame.draw.line(screen, colors_palet['PINK'], city.point, shadow_point, 2)
    text_render = font.render(other_city.name, True, colors_palet['WHITE'])
    text_point_x = shadow_point[0] if shadow_point[0] < 500 else shadow_point[0] - 220    
    text_point = (text_point_x, shadow_point[1] - 50)
    screen.blit(text_render, text_point)


def clculate_shadow_point(point, other_point):
    if point[0] < 500:
        shadow_point = (0, other_point[1] // 2)

    else:
        shadow_point = (2000, point[1])

    return shadow_point
