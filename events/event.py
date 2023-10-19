import pygame
from events import bord_map
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
CLICK_ON_CARD = pygame.USEREVENT + 11
CLICK_ON_CITY = pygame.USEREVENT + 12
player_1 = pygame.USEREVENT + 13
player_2 = pygame.USEREVENT + 14
player_3 = pygame.USEREVENT + 15
player_4 = pygame.USEREVENT + 16

bottons_events = {'switch_bord_to_map' : pygame.USEREVENT + 1,
                  'direct_flight' : pygame.USEREVENT + 2,
                  'discover_cure' : pygame.USEREVENT + 3,
                  'share_knowledge' : pygame.USEREVENT + 4,
                  'cure_blue' : pygame.USEREVENT + 5,
                  'cure_yellow' : pygame.USEREVENT + 6,
                  'cure_black' : pygame.USEREVENT + 7,
                  'cure_red' : pygame.USEREVENT + 8,
                  'builed_research_station' : pygame.USEREVENT + 9,
                  'switch_bord_to_cards' : pygame.USEREVENT + 10,
                  'player 1' : pygame.USEREVENT + 13,
                  'player 2' : pygame.USEREVENT + 14,
                  'player 3' : pygame.USEREVENT + 15,
                  'player 4' : pygame.USEREVENT + 16,

}


def handel_event(event, cities, corent_player, bord_state, players, all_bottons, player_input):
    my_bottons = all_bottons[player_input['corent_page']]
    if player_input['corent_page'] == 'map':
        player_input['chosen_city'] = bord_map.clicked_on_city(cities, corent_player, bord_state, player_input['chosen_city'], event)

   
    if player_input['corent_page'] == 'cards':
        for player in players:
            for card in player.hand:
                player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    for botton in my_bottons:
        botton.handle_event(event)

    if event.type == CURE_BLUE:
        treat_diseasse(bord_state, corent_player, 'BLUE')
   
    elif event.type == CURE_YELLOW:
        treat_diseasse(bord_state, corent_player, 'YELLOW')

    elif event.type == CURE_BLACK:
        treat_diseasse(bord_state, corent_player, 'BLACK')

    elif event.type == CURE_RED:
        treat_diseasse(bord_state, corent_player, 'RED')

    elif event.type == SWITCH_BORD_TO_CARDS:
        player_input['corent_page'] = 'cards'

    elif event.type == SWITCH_BORD_TO_MAP:
        player_input['corent_page'] = 'map'

    elif event.type == BUILED_RESEARCH_STATION:
        builed_research_station(bord_state, corent_player, cities)

    elif event.type == SHARE_KNOWLEDGE:
        picked_player = player_input['picked_player']
        picked_cards = player_input['picked_cards']
        share_knowledge(corent_player, picked_player, picked_cards)
        player_input['picked_cards'] = reset_picked_cards(picked_cards)
        player_input['picked_player'] = None

    elif event.type == DISCOVER_CURE:
        picked_cards = player_input['picked_cards']
        discover_cure(bord_state, picked_cards, corent_player)
        player_input['picked_cards'] = reset_picked_cards(picked_cards)


    elif event.type == DIRECT_FLIGHT:
        picked_cards = player_input['picked_cards']
        direct_flight(bord_state, corent_player, picked_cards, cities)
        player_input['picked_cards'] = reset_picked_cards(picked_cards)
    
    elif event.type == CLICK_ON_CARD:
        for i, card in enumerate(player_input['picked_cards']):
            if card == player_input['chosen_card']:
                player_input['picked_cards'].pop(i)
                player_input['chosen_card'].picked = False
                break

        else:
            player_input['chosen_card'].picked = True
            player_input['picked_cards'].append(player_input['chosen_card'])

    elif event.type == CLICK_ON_CITY:
        corent_player.corent_city = player_input['chosen_city']
        player_input['chosen_city'] = None
        corent_player.actions -= 1

    elif event.type == player_1:
        player_input['picked_player'] = players[0]
    
    elif event.type == player_2:
        player_input['picked_player'] = players[1]
    
    elif event.type == player_3:
        player_input['picked_player'] = players[2]
    
    elif event.type == player_4:
        player_input['picked_player'] = players[3]

    return player_input


def reset_picked_cards(picked_cards):
    for card in picked_cards:
        card.picked = False
    
    return []
       
