import pygame
from events import bord_map
from lib import treat_diseasse, builed_research_station, share_knowledge, discover_cure, direct_flight, infected_phase, draw_from_deck, move_to_city
from data import ACTION_PER_TURN

END_TURN = pygame.USEREVENT + 1
SWITCH_BORD_TO_MAP = pygame.USEREVENT + 2
DIRECT_FLIGHT = pygame.USEREVENT + 3
DISCOVER_CURE = pygame.USEREVENT + 4
SHARE_KNOWLEDGE = pygame.USEREVENT + 5
CURE_BLUE = pygame.USEREVENT + 6
CURE_YELLOW = pygame.USEREVENT + 7
CURE_BLACK = pygame.USEREVENT + 8
CURE_RED = pygame.USEREVENT + 9
BUILED_RESEARCH_STATION = pygame.USEREVENT + 10
SWITCH_BORD_TO_CARDS = pygame.USEREVENT + 11
CLICK_ON_CARD = pygame.USEREVENT + 12
CLICK_ON_CITY = pygame.USEREVENT + 13
MOVE_TO_CITY = pygame.USEREVENT + 14
PLAYER_1 = pygame.USEREVENT + 15
PLAYER_2 = pygame.USEREVENT + 16
PLAYER_3 = pygame.USEREVENT + 17
PLAYER_4 = pygame.USEREVENT + 18
USE_EVENT_CARD = pygame.USEREVENT + 19
ONE_QUIET_NIGHT = pygame.USEREVENT + 20
RESILIENT_POPULATION = pygame.USEREVENT + 21
FORECAST = pygame.USEREVENT + 22
GOVERNMENT_GRANT = pygame.USEREVENT + 23
AIRLIFT = pygame.USEREVENT + 24
APPLY_FORECAST = pygame.USEREVENT + 25
APPLY_RESILIENT_POPULATION = pygame.USEREVENT + 26

bottons_events = {'switch_bord_to_map' : SWITCH_BORD_TO_MAP,
                  'direct_flight' : DIRECT_FLIGHT,
                  'discover_cure' : DISCOVER_CURE,
                  'share_knowledge' : SHARE_KNOWLEDGE,
                  'cure_blue' : CURE_BLUE,
                  'cure_yellow' : CURE_YELLOW,
                  'cure_black' : CURE_BLACK,
                  'cure_red' : CURE_RED,
                  'builed_research_station' : BUILED_RESEARCH_STATION,
                  'switch_bord_to_cards' : SWITCH_BORD_TO_CARDS,
                  'player 1' : PLAYER_1,
                  'player 2' : PLAYER_2,
                  'player 3' : PLAYER_3,
                  'player 4' : PLAYER_4,
                  'use_event_card' : USE_EVENT_CARD,
                  'apply_forcast' : APPLY_FORECAST,
                  'apply_resilient_population' : APPLY_RESILIENT_POPULATION}

events_cards_events = {'one quiet night' : ONE_QUIET_NIGHT,
                       'resilient population' : RESILIENT_POPULATION,
                       'forecast' : FORECAST,
                       'airlift' : AIRLIFT,
                       'government grant' : GOVERNMENT_GRANT}

def handel_event(event, cities, cycle_player, corent_player, bord_state, players, all_bottons, player_input):
    my_bottons = all_bottons[player_input['corent_page']]
    if player_input['corent_page'] == 'map':
        player_input['chosen_city'] = bord_map.clicked_on_city(cities, corent_player, bord_state, player_input['chosen_city'], event, player_input['unlimited_movement'])
        if player_input['chosen_city']: player_input['unlimited_movement'] = False
   
    if player_input['corent_page'] == 'cards':
        for player in players:
            for card in player.hand:
                player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    if player_input['corent_page'] == 'forecast':
        for card in bord_state.infaction_cards[:6]:
            player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    if player_input['corent_page'] == 'resilient_population':
        for card in bord_state.infaction_discard_cards:
            player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    for botton in my_bottons:
        botton.handle_event(event)

    if event.type == END_TURN:
        draw_from_deck(bord_state, corent_player, cities)
        if not player_input['one_quiet_night']: infected_phase(bord_state, cities)
        corent_player = next(cycle_player)
        corent_player.actions = ACTION_PER_TURN
        player_input['one_quiet_night'] = False


    elif event.type == CURE_BLUE:
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
        government_grant = player_input['government_grant']
        chosen_city = player_input['chosen_city'] 
        builed_research_station(bord_state, corent_player, cities, government_grant, chosen_city)
        player_input['government_grant'] = False
        player_input['chosen_city'] = None

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
        player_input['unlimited_movement'] = direct_flight(bord_state, corent_player, picked_cards, cities)
        player_input['picked_cards'] = reset_picked_cards(picked_cards)
    
    elif event.type == CLICK_ON_CARD:
        player_input = pick_or_unpick_a_card(player_input)

    elif event.type == CLICK_ON_CITY:
        if player_input['government_grant']:
            pygame.event.post(pygame.event.Event(BUILED_RESEARCH_STATION))
                    
        else:
            pygame.event.post(pygame.event.Event(MOVE_TO_CITY))

    elif event.type == MOVE_TO_CITY:
        airlift = player_input['airlift']
        picked_player = player_input['picked_player']
        chosen_city = player_input['chosen_city']
        move_to_city(bord_state, chosen_city, corent_player, airlift, picked_player)
        player_input['chosen_city'] = None
        player_input['airlift'] = False
        player_input['picked_player'] = None

    elif event.type == PLAYER_1:
        player_input['picked_player'] = players[0]
    
    elif event.type == PLAYER_2:
        player_input['picked_player'] = players[1]
    
    elif event.type == PLAYER_3:
        player_input['picked_player'] = players[2]
    
    elif event.type == PLAYER_4:
        player_input['picked_player'] = players[3]

    elif event.type == USE_EVENT_CARD:
        # distroyed if push for no reson!!!! (no picked card)
        event_card = player_input['picked_cards'][0]
        event_card.use_event_card()            
        discard_card(players, event_card, bord_state)

    elif event.type == ONE_QUIET_NIGHT:
        player_input['one_quiet_night'] = True

    elif event.type == RESILIENT_POPULATION:
        player_input['corent_page'] = 'resilient_population'

    elif event.type == APPLY_RESILIENT_POPULATION:
        print('apply_resilient_population')
        if len(player_input['picked_cards']) == 1:
            for i, card in enumerate(bord_state.infaction_discard_cards):
                if card == player_input['picked_cards'][0]:
                    bord_state.infaction_discard_cards.pop(i)

            player_input['corent_page'] = 'map'

    elif event.type == FORECAST:
        player_input['corent_page'] = 'forecast'

    elif event.type == APPLY_FORECAST:
        bord_state.infaction_cards = player_input['picked_cards'] + bord_state.infaction_cards[6:]
        player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
        player_input['corent_page'] = 'map'

    elif event.type == AIRLIFT:
        player_input['unlimited_movement'] = True
        player_input['airlift'] = True
        player_input['corent_page'] = 'map'

    elif event.type == GOVERNMENT_GRANT:
        player_input['government_grant'] = True
        player_input['unlimited_movement'] = True
        player_input['corent_page'] = 'map'

    return player_input, corent_player


def reset_picked_cards(picked_cards):
    for card in picked_cards:
        card.picked = False
    
    return []
       
def pick_or_unpick_a_card(player_input):
    for i, card in enumerate(player_input['picked_cards']):
        if card == player_input['chosen_card']:
            player_input['picked_cards'].pop(i)
            player_input['chosen_card'].picked = False
            break

    else:
        player_input['chosen_card'].picked = True
        player_input['picked_cards'].append(player_input['chosen_card'])

    return player_input

def discard_card(players, discard_card, bord_state):
    for player in players:
        for i, card in enumerate(player.hand):
            if card == discard_card:
                player.hand.pop(i)   
                bord_state.player_discard_cards.append(discard_card)