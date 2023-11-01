import pygame
import data
from .event import all_events
import lib
from itertools import cycle
import sys




def handel_event(event, cities, cycle_player, bord_state, players, all_bottons, player_input):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    handel_bottons_events(event, all_bottons, player_input['corent_page'])
    if player_input['corent_page'] == 'map':
        player_input = handel_map_events(event, cities, bord_state, player_input, players)
    
    elif player_input['corent_page'] == 'map_dubel_epidemic':
        player_input = handel_map_dubel_epidemic_events(event, cities, bord_state, player_input, players)


    elif player_input['corent_page'] == 'cards':
        player_input = handel_cards_events(event, players, player_input)

    elif player_input['corent_page'] == 'forecast':
        player_input = handel_forcast_events(event, bord_state, player_input)

    elif player_input['corent_page'] == 'resilient_population':
        player_input = handel_resilient_population_events(event, bord_state, player_input)

    elif player_input['corent_page'] == 'operation_expert_discard_events_cards':
        player_input = handel_operation_expert_discard_events_cards_events(event, bord_state, player_input)

    elif player_input['corent_page'] == 'hand_limit':
        player_input = handel_hand_limit_events(event, player_input)

    elif player_input['corent_page'] == 'hand_limit_end_turn':
        player_input = handel_hand_limit_end_turn_events(event, player_input)

    elif player_input['corent_page'] == 'play_event_during_epidemic':
        player_input = play_event_during_epidemic_events(event, player_input, players)

    if event.type == all_events['END_TURN']:
        player_input = end_turn(player_input, bord_state, cities, players)

    elif event.type == all_events['CURE_BLUE']:
        lib.treat_diseasse(bord_state, player_input['corent_player'], 'BLUE')

    elif event.type == all_events['CURE_YELLOW']:
        lib.treat_diseasse(bord_state, player_input['corent_player'], 'YELLOW')

    elif event.type == all_events['CURE_BLACK']:
        lib.treat_diseasse(bord_state, player_input['corent_player'], 'BLACK')

    elif event.type == all_events['CURE_RED']:
        lib.treat_diseasse(bord_state, player_input['corent_player'], 'RED')

    elif event.type == all_events['SWITCH_BORD_TO_CARDS']:
        player_input['corent_page'] = 'cards'

    elif event.type == all_events['SWITCH_BORD_TO_MAP']:
        player_input = switch_to_bord_map(player_input)

    elif event.type == all_events['DISPLAY_INFACTION_DISCARD_CARD']:
        player_input['corent_page'] = 'infaction_discard_cards'

    elif event.type == all_events['DISPLAY_PLAYER_DISCARD_CARD']:
        player_input['corent_page'] = 'discard_player_cards'

    elif event.type == all_events['DISPLAY_CONTINGENCY_PLANNER_DISCARD_CARD']:
        player_input['corent_page'] = 'operation_expert_discard_events_cards'

    elif event.type == all_events['BUILED_RESEARCH_STATION']:
        builed_research_station(bord_state, cities, player_input)

    elif event.type == all_events['SHARE_KNOWLEDGE']:
        player_input = share_knowledge(player_input)

    elif event.type == all_events['DISCOVER_CURE']:
        player_input = discover_cure(player_input, bord_state, players)
        
    elif event.type == all_events['DIRECT_FLIGHT']:
        player_input = direct_flight(player_input, bord_state, cities)
        
    elif event.type == all_events['CLICK_ON_CARD']:
        player_input = pick_or_unpick_a_card(player_input)


    elif event.type == all_events['CLICK_ON_CITY']:
        if player_input['government_grant']:
            pygame.event.post(pygame.event.Event(all_events['BUILED_RESEARCH_STATION']))
            
        else:
            pygame.event.post(pygame.event.Event(all_events['MOVE_TO_CITY']))


    elif event.type == all_events['MOVE_TO_CITY']:
        player_input = move_to_city(player_input, bord_state)


    elif event.type == all_events['PLAYER_1']:
        player_input['picked_player'] = players[0]
    

    elif event.type == all_events['PLAYER_2']:
        player_input['picked_player'] = players[1]
    

    elif event.type == all_events['PLAYER_3']:
        player_input['picked_player'] = players[2]
    

    elif event.type == all_events['PLAYER_4']:
        player_input['picked_player'] = players[3]


    elif event.type == all_events['USE_EVENT_CARD']:
        player_input = use_event_card(player_input, players, bord_state)


    elif event.type == all_events['ONE_QUIET_NIGHT']:
        player_input['one_quiet_night'] = True


    elif event.type == all_events['RESILIENT_POPULATION']:
        player_input = resilient_population(player_input)


    elif event.type == all_events['APPLY_RESILIENT_POPULATION']:
        player_input = apply_resilient_population(player_input, bord_state)

    elif event.type == all_events['FORECAST']:
        player_input = forecast(player_input)

    elif event.type == all_events['APPLY_FORECAST']:
        player_input = apply_forecast_population(player_input, bord_state)

    elif event.type == all_events['AIRLIFT']:
        player_input = airlift(player_input)

    elif event.type == all_events['GOVERNMENT_GRANT']:
        player_input = government_grant(player_input)

    elif event.type == all_events['CONTINGENCY_PLANNER_TAKE_DISCARD_CARD']:    
        player_input = contingency_planner_take_event_card(player_input, bord_state)

    elif event.type == all_events['APPLY_HAND_LIMIT']:
        player_input = apply_hand_limit(player_input, bord_state)


    elif event.type == all_events['END_GAME_HAND_LIMIT']:
        player_input = end_game_hand_limit(player_input, bord_state)


    elif event.type == all_events['APPLY_END_GAME_HAND_LIMIT']:
        player_input = aplly_end_game_hand_limit(player_input, bord_state)

    elif event.type == all_events ['INFACTION_PHASE']:
        player_input = infaction_phase(player_input, bord_state, cities)

    elif event.type == all_events ['EPIDEMIC']:
        player_input = epidemic(player_input, bord_state, cities)

    elif event.type == all_events['NEXT_PLAYER']:
        player_input = next_player(player_input, cycle_player)

    elif event.type == all_events ['PLAYERS_MAY_PLAY_EVENT']:
        player_input = players_may_play_event(player_input, bord_state, cities, players)

    return player_input


def handel_bottons_events(event, all_bottons, corent_page):
    my_bottons = all_bottons[corent_page]    
    for botton in my_bottons:
        botton.handle_event(event)


def handel_map_events(event, cities, bord_state, player_input, players):
    corent_player  = player_input['corent_player']
    player_input = which_city_clicked_on(cities, bord_state, player_input, event, players)
    if bord_state.infaction_discard_cards: 
        bord_state.infaction_discard_cards[-1].handle_discard_event(event)
    
    if bord_state.player_discard_cards: 
        bord_state.player_discard_cards[-1].handle_discard_event(event, corent_player)

    return player_input

def handel_map_dubel_epidemic_events(event, cities, bord_state, player_input, players):
    player_input = which_city_clicked_on(cities, bord_state, player_input, event, players)
    return player_input

def which_city_clicked_on(cities, bord_state, player_input, event, players):
    corent_player = player_input['corent_player']
    chosen_city = player_input['chosen_city'] 
    unlimited_movement = player_input['unlimited_movement']
    picked_player = player_input['picked_player']
    routes = []
    moving_player, extra_routes = dispatcher_movment(corent_player, picked_player, players)
    routes += extra_routes
    routes += get_routes(cities, moving_player, bord_state, unlimited_movement)
    for city_name in set(routes):
        city = cities[city_name]
        chosen_city = city.handle_event(event, chosen_city)

    player_input['chosen_city'] = chosen_city 
    if chosen_city: player_input['unlimited_movement'] = False
    if chosen_city: player_input['active_event'] = False
    return player_input


def get_routes(cities, moving_player, bord_state, unlimited_movement):
    if unlimited_movement: routes = [city.name for city in cities.values()]
    
    else:
        corent_city = moving_player.corent_city
        routes = corent_city.routes.copy()
        if corent_city.research_station:
            routes += get_reserch_station_cities(bord_state, corent_city) 

    return routes


def get_reserch_station_cities(bord_state, corent_city):
    research_stations_cities = bord_state.research_stations.copy()
    for i, city_name in enumerate(research_stations_cities):
        if corent_city.name == city_name:
            research_stations_cities.pop(i)

    return research_stations_cities 


def dispatcher_movment(corent_player, picked_player, players):
    moving_player = dispacher_choose_player_to_move(corent_player, picked_player)
    if corent_player.role == 'Dispatcher':
        extra_routes = [player.corent_city.name for player in players if player.corent_city != moving_player.corent_city] 
    
    else:
        extra_routes = []

    return moving_player, extra_routes        


def dispacher_choose_player_to_move(corent_player, picked_player):
    if corent_player.role == 'Dispatcher' and picked_player:
        moving_player = picked_player 

    else:
        moving_player = corent_player 
    
    return  moving_player        


def handel_cards_events(event, players, player_input):
    for player in players:
        if player.role == 'Contingency_Planner':
            if player.contingency_planner_event_card: 
                player_input['chosen_card'] = player.contingency_planner_event_card.handle_event(event, player_input['chosen_card']) 

        for card in player.hand:
            player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    return player_input

def handel_hand_limit_events(event, player_input):
    player = player_input['picked_player']
    for card in player.hand:
        player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    return player_input

def play_event_during_epidemic_events(event, player_input, players):
    for player in players:
        if player.role == 'Contingency_Planner':
            if player.contingency_planner_event_card: 
                player_input['chosen_card'] = player.contingency_planner_event_card.handle_event(event, player_input['chosen_card']) 

        for card in player.hand:
            if type(card) == data.EventCard:
                player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    return player_input


def handel_forcast_events(event, bord_state, player_input):
    for card in bord_state.infaction_cards[:6]:
        player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    return player_input 


def handel_resilient_population_events(event, bord_state, player_input):
    for card in bord_state.infaction_discard_cards:
        player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])
    
    return player_input


def handel_operation_expert_discard_events_cards_events(event, bord_state, player_input):
    discard_event_cards = [card for card in bord_state.player_discard_cards if type(card) == data.EventCard]
    for card in discard_event_cards:
        player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    return player_input

def handel_hand_limit_end_turn_events(event, player_input):
    player_cards = [card for card in player_input['corent_player'].hand]
    for card in player_cards:
        player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])
    
    return player_input 

def switch_to_bord_map(player_input):
    if player_input['corent_page'] == 'operation_expert_discard_events_cards': 
        player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
    
    player_input['corent_page'] = 'map'
    return player_input


def builed_research_station(bord_state, cities, player_input):
    government_grant = player_input['government_grant']
    chosen_city = player_input['chosen_city']
    if len(player_input['picked_cards']) == 1: 
        picked_card = player_input['picked_cards'][0]
    
    else:
        picked_card = None

    lib.builed_research_station(bord_state, player_input['corent_player'], cities, government_grant, city_card=picked_card, builed_city=chosen_city)
    player_input['government_grant'] = False
    player_input['chosen_city'] = None
    player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
    if player_input['dubel_epidemic']: player_input['corent_page'] = 'play_event_during_epidemic'
    return player_input


def direct_flight(player_input, bord_state, cities):
    if not player_input['active_event']:
        picked_cards = player_input['picked_cards']
        picked_player = player_input['picked_player']
        corent_player = player_input['corent_player']
        player_input['unlimited_movement'] = lib.direct_flight(bord_state, corent_player, picked_cards, cities, picked_player)
        player_input['picked_cards'] = reset_picked_cards(picked_cards)
        if not player_input['unlimited_movement']: player_input['picked_player'] = None
    
    return player_input         

def share_knowledge(player_input):
    if not player_input['active_event']:
        corent_player = player_input['corent_player']    
        picked_player = player_input['picked_player']
        picked_cards = player_input['picked_cards']
        lib.share_knowledge(corent_player, picked_player, picked_cards)
        if len(corent_player.hand) > data.HAND_LIMIT: 
            player_input['corent_page'] = 'hand_limit'
            player_input['picked_player'] = corent_player

        if len(picked_player.hand) > data.HAND_LIMIT: 
            player_input['corent_page'] = 'hand_limit'
            player_input['picked_player'] = picked_player

        player_input['picked_cards'] = reset_picked_cards(picked_cards)

    return player_input 


def discover_cure(player_input, bord_state, players):
    if not player_input['active_event']:    
        picked_cards = player_input['picked_cards']
        corent_player = player_input['corent_player']
        lib.discover_cure(bord_state, picked_cards, corent_player)
        for player in players:
            if player.role == 'Medic':
                lib.clear_discovered_cure_diseasse(bord_state, player)

        player_input['picked_cards'] = reset_picked_cards(picked_cards)

    return player_input


def use_event_card(player_input, players, bord_state):
    if (not player_input['active_event'] and 
        len(player_input['picked_cards']) == 1 and
        type(player_input['picked_cards'][0]) == data.EventCard and
        (player_input['dubel_epidemic'] and player_input['picked_cards'][0].name != 'resilient population')):
        event_card = player_input['picked_cards'][0]

        for player in players:
            if event_card == player.contingency_planner_event_card:
                player.contingency_planner_event_card = None
        
            else:    
                discard_event_card(players, event_card, bord_state)
            
            event_card.use_event_card() 

    player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
    return player_input


def airlift(player_input):
    player_input['unlimited_movement'] = True
    player_input['airlift'] = True
    player_input['active_event'] = True
    player_input['corent_page'] = 'map'
    if player_input['dubel_epidemic']: player_input['corent_page'] = 'map_dubel_epidemic'

    return player_input


def government_grant(player_input):
    player_input['active_event'] = True
    player_input['government_grant'] = True
    player_input['unlimited_movement'] = True
    player_input['corent_page'] = 'map'
    if player_input['dubel_epidemic']: player_input['corent_page'] = 'map_dubel_epidemic'
    return player_input


def resilient_population(player_input):
    player_input['corent_page'] = 'resilient_population'
    player_input['active_event'] = True


def apply_resilient_population(player_input, bord_state):
    if len(player_input['picked_cards']) == 1:
        for i, card in enumerate(bord_state.infaction_discard_cards):
            if card == player_input['picked_cards'][0]:
                bord_state.infaction_discard_cards.pop(i)
                player_input['corent_page'] = 'map'
                player_input['active_event'] = False

    return player_input


def forecast(player_input):
    player_input['corent_page'] = 'forecast'
    return player_input


def apply_forecast_population(player_input, bord_state):
    if len(player_input['picked_cards']) == 6:
        bord_state.infaction_cards = player_input['picked_cards'] + bord_state.infaction_cards[6:]
        player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
        player_input['corent_page'] = 'map'
        if player_input['dubel_epidemic']: player_input['corent_page'] = 'play_event_during_epidemic'

    return player_input


def contingency_planner_take_event_card(player_input, bord_state):
    corent_player = player_input['corent_player']
    picked_cards = player_input['picked_cards']
    if (len(player_input['picked_cards']) == 1 and
        corent_player.role == 'Contingency_Planner'):
        lib.contingency_planner_take_event_card(corent_player, picked_cards, bord_state)
        player_input['corent_page'] = 'map'

    player_input['picked_cards'] = reset_picked_cards(picked_cards)
    return  player_input


def move_to_city(player_input, bord_state):
    airlift = player_input['airlift']
    picked_player = player_input['picked_player']
    chosen_city = player_input['chosen_city']
    corent_player = player_input['corent_player']
    lib.move_to_city(bord_state, chosen_city, corent_player, airlift, picked_player)
    player_input['chosen_city'] = None
    player_input['airlift'] = False
    player_input['picked_player'] = None
    if player_input['dubel_epidemic']: player_input['corent_page'] = 'play_event_during_epidemic'

    return player_input


def end_turn(player_input, bord_state, cities, players):
    one_quiet_night = player_input['one_quiet_night']
    corent_player = player_input['corent_player']
    player_input['quarantined_cities'] = lib.quarantine_specialist_effect(players)
    number_of_epidemics = lib.draw_from_deck(bord_state, corent_player, cities)
    if number_of_epidemics == 2:
        #epidemic -> event card option -> epidemic -> infaction -> next_player
         end_turn_sequence = ['EPIDEMIC','PLAYERS_MAY_PLAY_EVENT', 'EPIDEMIC', 'INFACTION_PHASE', 'NEXT_PLAYER']
         player_input['dubel_epidemic'] = True

    if number_of_epidemics == 1:
        #hand limit chack -> epidemic -> infaction -> next_player
         end_turn_sequence = ['EPIDEMIC', 'INFACTION_PHASE', 'NEXT_PLAYER']

    elif number_of_epidemics == 0:
        # hand limit chack -> infaction -> next_player
         end_turn_sequence = ['INFACTION_PHASE', 'NEXT_PLAYER']
    
    player_input['end_turn_sequence'] = cycle(end_turn_sequence)
    pygame.event.post(pygame.event.Event(all_events['END_GAME_HAND_LIMIT']))
    return player_input


def end_game_hand_limit(player_input, bord_state):
    corent_player = player_input['corent_player']
    if len(corent_player.hand) > data.HAND_LIMIT:
        player_input['corent_page'] = 'hand_limit_end_turn'

    else:
        player_input['corent_page'] = 'map'
        next_end_game_phase = next(player_input['end_turn_sequence'])
        pygame.event.post(pygame.event.Event(all_events[next_end_game_phase]))

    return player_input 


def infaction_phase(player_input, bord_state, cities):
    if not player_input['one_quiet_night']: lib.infected_phase(bord_state, cities, player_input['quarantined_cities'])

    player_input['one_quiet_night'] = False
    next_end_game_phase = next(player_input['end_turn_sequence'])
    pygame.event.post(pygame.event.Event(all_events[next_end_game_phase]))
    return player_input

def next_player(player_input, cycle_player):
    player_input['corent_player'] = lib.next_player(cycle_player)
    player_input['dubel_epidemic'] = False
    player_input['corent_page'] = 'map'
    return player_input


def apply_hand_limit(player_input, bord_state):
    if len(player_input['picked_cards']) == 1:
        print('apply_hand_limit')
        discard_card = player_input['chosen_card']
        corent_player = player_input['corent_player']
        player_input = pick_or_unpick_a_card(player_input)
        discard_one_card(corent_player, discard_card, bord_state)
        player_input['chosen_card'].picked = False
        player_input['corent_page'] = 'cards'

    return player_input
    


def aplly_end_game_hand_limit(player_input, bord_state):
    discard_card = player_input['chosen_card']
    corent_player = player_input['corent_player']
    player_input = pick_or_unpick_a_card(player_input)
    discard_one_card(corent_player, discard_card, bord_state)
    pygame.event.post(pygame.event.Event(all_events['END_GAME_HAND_LIMIT']))
    return player_input


def epidemic(player_input, bord_state, cities):
    quarantined_cities = player_input['quarantined_cities']
    lib.epidemic_effect(bord_state, cities, quarantined_cities)
    next_end_game_phase = next(player_input['end_turn_sequence'])
    pygame.event.post(pygame.event.Event(all_events[next_end_game_phase]))
    return player_input 


def players_may_play_event(player_input, bord_state, cities, players):
    player_input['corent_page'] = 'play_event_during_epidemic'
    return player_input


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


def discard_event_card(players, discard_card, bord_state):
    for player in players:
        discard_one_card(player, discard_card, bord_state)


def discard_one_card(player, discard_card, bord_state):
    for i, card in enumerate(player.hand):
        if card == discard_card:
            player.hand.pop(i)   
            bord_state.player_discard_cards.append(discard_card)

