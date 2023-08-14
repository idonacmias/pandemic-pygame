from .constances import CITY_RADIUS
from .color import colors_palet
import pygame



def draw(city, screen, color):
    player_point = (city.point[0], city.point[1] + 0.5 * CITY_RADIUS)  
    pygame.draw.circle(surface=screen, color=colors_palet[color], center=player_point , radius=CITY_RADIUS * 0.25)


    player_point = (city.point[0], city.point[1] - 0.5 * CITY_RADIUS)  
    pygame.draw.circle(surface=screen, color=colors_palet[color], center=player_point , radius=CITY_RADIUS * 0.25)

    player_point = (city.point[0] - 0.5 * CITY_RADIUS, city.point[1])  
    pygame.draw.circle(surface=screen, color=colors_palet[color], center=player_point , radius=CITY_RADIUS * 0.25)

    player_point = (city.point[0] + 0.5 * CITY_RADIUS, city.point[1])  
    pygame.draw.circle(surface=screen, color=colors_palet[color], center=player_point , radius=CITY_RADIUS * 0.25)
