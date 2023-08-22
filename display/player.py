from .constances import CITY_RADIUS
from .color import colors_palet
import pygame


def convert_player_to_cities_dict(players):
    player_positin = {}
    for player in players:
        try:
            player_positin[player.corent_city_name].append(player.color)

        except KeyError:
            player_positin.update({player.corent_city_name : [player.color]})

    return player_positin

def draw(cities, screen, players):
    player_cities = convert_player_to_cities_dict(players)
    for city_name in player_cities.keys():
        for i, player_color in enumerate(player_cities[city_name]):
            player_point = (positions(cities[city_name].point, i))  
            pygame.draw.circle(surface=screen, color=player_color, center=player_point , radius=CITY_RADIUS * 0.25)

def positions(point, player_num):
    positions = [(point[0], point[1] - 0.5 * CITY_RADIUS),(point[0] + 0.5 * CITY_RADIUS, point[1]) ,(point[0], point[1] + 0.5 * CITY_RADIUS), (point[0] - 0.5 * CITY_RADIUS, point[1])]
    return positions[player_num]