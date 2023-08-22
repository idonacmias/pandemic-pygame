import pygame

from .color import colors_palet
from .constances import CITY_RADIUS, EDGE_CITIES




def draw(city, screen, font):
    color = colors_palet[city.color.name]
    pygame.draw.circle(surface=screen, color=color, center=city.point , radius=CITY_RADIUS)
    if city.resarch_station:
        pygame.draw.circle(surface=screen, color=colors_palet['WHITE'], center=city.point , radius=10)

    font_point = (city.point[0] - 5 * len(city.name), city.point[1] + 20)        
    text_surface = font.render(city.name, True, colors_palet['WHITE']) 
    screen.blit(text_surface, font_point)

def conect_routes(city, screen, cities, font):
    for other_city_name in city.routes:
        other_city_point = cities[other_city_name].point
        if is_edge_conection(city, other_city_point):
            shadow_point = clculate_shadow_point(city.point, other_city_point)
            pygame.draw.line(screen, colors_palet['PINK'], city.point, shadow_point, 2)

            text_render = font.render(other_city_name, True, colors_palet['WHITE'])
            text_point_x = shadow_point[0] if shadow_point[0] < 500 else shadow_point[0] - 220    
            text_point = (text_point_x, shadow_point[1] - 50)
            screen.blit(text_render, text_point)

        else:
            other_city = cities[other_city_name]
            pygame.draw.line(screen, colors_palet['PINK'], city.point, other_city.point, 2)

def is_edge_conection(city, other_city_point):
    return city.name in EDGE_CITIES and abs(other_city_point[0] - city.point[0]) > 500

def clculate_shadow_point(point, other_point):
    if point[0] < 500:
        shadow_point = (0, other_point[1] // 2)

    else:
        shadow_point = (2000, point[1])

    return shadow_point

def click_lenth_from_center(city, mouse_point):
    return abs(city.point[0] - mouse_point[0]) + abs(city.point[1] - mouse_point[1])
