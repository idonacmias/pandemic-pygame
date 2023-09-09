import pygame
from events import bord_map, bord_cards
from display import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS



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
        bord_map.clicked_on_city(cities, players, corent_player, mouse_point)
        button_data = zip(MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS)
        botton_clicked = witch_click_on(mouse_point, button_data)
        corent_page = bord_map.click_on_botton(cities, players, corent_player, botton_clicked)
        return corent_page



def handel_cards_events(event, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        buttons_data = zip(CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS)
        botton_clicked = witch_click_on(mouse_point, buttons_data)
        corent_page = bord_cards.click_on_botton(cities, players, corent_player, botton_clicked)
        return corent_page



def witch_click_on(mouse_point, buttons_data):
    for button_point, text in buttons_data:   
        square_points = [button_point, (button_point[0] + BUTTON_WHIDTH, button_point[1] + BUTTON_HIGHT)]
        if is_in_squer(square_points, mouse_point):
            return text                 


def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]