import pygame
from events import bord_map, bord_cards
from display import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS
from lib import treat_diseasse, builed_research_station, share_knowledge, discover_cure, direct_flight



SWITCH_BORD_TO_MAP = pygame.USEREVENT + 1
DIRECT_FLIGHT = pygame.USEREVENT + 2
DISCOVER_CURE = pygame.USEREVENT + 3
SHARE_KNOWLEDGE = pygame.USEREVENT + 4
CURE_BLUE = pygame.USEREVENT + 5
CURE_YELLOW = pygame.USEREVENT + 6
CURE_BLACK = pygame.USEREVENT + 7
CURE_RED = pygame.USEREVENT + 8
BUILED_RESEARCH_STATION = pygame.USEREVENT + 9
SWITCH_BORD_TO_CARDS = pygame.USEREVENT + 10

user_events = {'switch_bord_to_map' : SWITCH_BORD_TO_MAP,
               'direct_flight' : DIRECT_FLIGHT,
               'discover_cure' : DISCOVER_CURE,
               'share_knowledge' : SHARE_KNOWLEDGE,
               'cure_blue' : CURE_BLUE,
               'cure_yellow' : CURE_YELLOW,
               'cure_black' : CURE_BLACK,
               'cure_red' : CURE_RED,
               'builed_research_station' : BUILED_RESEARCH_STATION,
               'switch_bord_to_cards' : SWITCH_BORD_TO_CARDS
}


def handel_event(event, corent_page, cities, picked_player, corent_player, bord_state, picked_cards, players, all_buttons):
    my_buttons = all_buttons[corent_page]
    if corent_page == 'map':
        corent_page = handel_map_events(event, cities, corent_player, bord_state, my_buttons)
   
    # elif corent_page == 'cards':
        # corent_page, piked_cards, picked_player = handel_cards_events(event, cities, piked_player, corent_player, piked_cards, bord_state, players, my_buttons)



    for button in my_buttons:
        button.handle_event(event)

    if event.type == CURE_BLUE:
        treat_diseasse(bord_state, corent_player, 'BLUE')
   
    elif event.type == CURE_YELLOW:
        treat_diseasse(bord_state, corent_player, 'YELLOW')

    elif event.type == CURE_BLACK:
        treat_diseasse(bord_state, corent_player, 'BLACK')

    elif event.type == CURE_RED:
        treat_diseasse(bord_state, corent_player, 'RED')

    elif event.type == SWITCH_BORD_TO_CARDS:
        corent_page = 'cards'

    elif event.type == SWITCH_BORD_TO_MAP:
        corent_page = 'map'

    elif event.type == BUILED_RESEARCH_STATION:
        builed_research_station(bord_state, corent_player, cities)

    elif event.type == SHARE_KNOWLEDGE:
        print('need to implement: picked_player, picked_cards')
        # print(corent_player, picked_player, picked_cards)
        # share_knowledge(corent_player, picked_player, picked_cards)
        # picked_cards = []
        # picked_player = None

    elif event.type == DISCOVER_CURE:
        print('need to implement: picked_player, picked_cards')
        # discover_cure(bord_state, picked_cards, corent_player)
        # picked_cards = []

    elif event.type == DIRECT_FLIGHT:
        print('need to implement: picked_player, picked_cards')
        # direct_flight(corent_player, picked_cards)
        # picked_cards = []


    return corent_page, picked_cards, picked_player


def handel_map_events(event, cities, corent_player, bord_state, my_buttons):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        bord_map.clicked_on_city(cities, corent_player, mouse_point, bord_state)
   

       
        # botton_clicked = witch_button_click_on(mouse_point, MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS)
        # corent_page = bord_map.click_on_botton(cities, corent_player, botton_clicked, bord_state)
        # return corent_page



# def handel_cards_events(event, cities, piked_player, corent_player, piked_cards, bord_state, players, my_buttons):
#     corent_page = None
#     if event.type == pygame.MOUSEBUTTONUP:
#         mouse_point = pygame.mouse.get_pos()
#         piked_player = bord_cards.clicked_on_player(mouse_point, piked_player, players)
#         piked_cards = bord_cards.witch_card_click_on(mouse_point, players, piked_cards)
#         botton_clicked = witch_button_click_on(mouse_point, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS)
#         corent_page, piked_cards, picked_player = bord_cards.click_on_botton(bord_state, corent_player, botton_clicked, piked_cards, piked_player)
    
#     return corent_page, piked_cards, piked_player



# def witch_button_click_on(mouse_point, buttons_point, buttons_text):
#     buttons_data = zip(buttons_point, buttons_text)
#     for button_point, text in buttons_data:   
#         square_points = [button_point, (button_point[0] + BUTTON_WHIDTH, button_point[1] + BUTTON_HIGHT)]
#         if is_in_squer(square_points, mouse_point):
#             return text                 


# def is_in_squer(square_points, point):
#     x = 0
#     y = 1
#     return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]