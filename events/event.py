import pygame
from .map import clicked_on_city, click_on_botton

def handel_event(event, corent_page, cities, players, corent_player):
    if corent_page == 'map':
        corent_page = handel_map_events(event, cities, players, corent_player)
   
    return corent_page

def handel_map_events(event, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        clicked_on_city(cities, players, corent_player, mouse_point)
        corent_page = click_on_botton(cities, players, corent_player, mouse_point)
        return corent_page