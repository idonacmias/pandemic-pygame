import pygame
from .bord_map import clicked_on_city, click_on_botton
import bord_cards



def handel_event(event, corent_page, cities, players, corent_player):
    if corent_page == 'map':
        corent_page = handel_map_events(event, cities, players, corent_player)
   
    elif corent_page == 'cards':
        corent_page = handel_cards_events(event, cities, players, corent_player)
        pass

    return corent_page


def handel_map_events(event, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        clicked_on_city(cities, players, corent_player, mouse_point)
        corent_page = click_on_botton(cities, players, corent_player, mouse_point)
        return corent_page



def handel_cards_events(event, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        corent_page = bord_cards.click_on_botton(cities, players, corent_player, mouse_point)
        return corent_page


