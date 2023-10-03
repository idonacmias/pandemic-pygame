import pygame
from events import bord_map, bord_cards
from display import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS


def handel_event(event, corent_page, cities, piked_player, corent_player, bord_state, piked_cards, players):
    if corent_page == 'map':
        corent_page = handel_map_events(event, cities, corent_player, bord_state)
   
    elif corent_page == 'cards':
        corent_page, piked_cards, piked_player = handel_cards_events(event, cities, piked_player, corent_player, piked_cards, bord_state, players)

    return corent_page, piked_cards, piked_player


def handel_map_events(event, cities, corent_player, bord_state):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        bord_map.clicked_on_city(cities, corent_player, mouse_point, bord_state)
        botton_clicked = witch_button_click_on(mouse_point, MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS)
        corent_page = bord_map.click_on_botton(cities, corent_player, botton_clicked, bord_state)
        return corent_page



def handel_cards_events(event, cities, piked_player, corent_player, piked_cards, bord_state, players):
    corent_page = None
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        piked_player = bord_cards.clicked_on_player(mouse_point, piked_player, players)
        piked_cards = bord_cards.witch_card_click_on(mouse_point, players, piked_cards)
        botton_clicked = witch_button_click_on(mouse_point, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS)
        corent_page, piked_cards, picked_player = bord_cards.click_on_botton(bord_state, corent_player, botton_clicked, piked_cards, piked_player)
    
    return corent_page, piked_cards, piked_player



def witch_button_click_on(mouse_point, buttons_point, buttons_text):
    buttons_data = zip(buttons_point, buttons_text)
    for button_point, text in buttons_data:   
        square_points = [button_point, (button_point[0] + BUTTON_WHIDTH, button_point[1] + BUTTON_HIGHT)]
        if is_in_squer(square_points, mouse_point):
            return text                 


def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]