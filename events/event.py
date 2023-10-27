import pygame
from events import bord_map
from lib import treat_diseasse, builed_research_station, share_knowledge, discover_cure, direct_flight, infected_phase, draw_from_deck, move_to_city, clear_discovered_cure_diseasse, contingency_planner_take_event_card
from data import ACTION_PER_TURN
import data


all_events_list = ['END_TURN',
                  'SWITCH_BORD_TO_MAP',
                  'DIRECT_FLIGHT',
                  'DISCOVER_CURE',
                  'SHARE_KNOWLEDGE',
                  'CURE_BLUE',
                  'CURE_YELLOW',
                  'CURE_BLACK',
                  'CURE_RED',
                  'BUILED_RESEARCH_STATION',
                  'SWITCH_BORD_TO_CARDS',
                  'CLICK_ON_CARD',
                  'CLICK_ON_CITY',
                  'MOVE_TO_CITY',
                  'PLAYER_1',
                  'PLAYER_2',
                  'PLAYER_3',
                  'PLAYER_4',
                  'USE_EVENT_CARD',
                  'ONE_QUIET_NIGHT',
                  'RESILIENT_POPULATION',
                  'FORECAST',
                  'GOVERNMENT_GRANT',
                  'AIRLIFT',
                  'APPLY_FORECAST',
                  'APPLY_RESILIENT_POPULATION',
                  'DISPLAY_INFACTION_DISCARD_CARD',
                  'DISPLAY_PLAYER_DISCARD_CARD',
                  'DISPLAY_CONTINGENCY_PLANNER_DISCARD_CARD',
                  'CONTINGENCY_PLANNER_TAKE_DISCARD_CARD']

all_events = {event_name : pygame.USEREVENT + i for i, event_name in enumerate(all_events_list)}


bottons_events = {'switch_bord_to_map' : all_events['SWITCH_BORD_TO_MAP'],
                  'direct_flight' : all_events['DIRECT_FLIGHT'],
                  'discover_cure' : all_events['DISCOVER_CURE'],
                  'share_knowledge' : all_events['SHARE_KNOWLEDGE'],
                  'cure_blue' : all_events['CURE_BLUE'],
                  'cure_yellow' : all_events['CURE_YELLOW'],
                  'cure_black' : all_events['CURE_BLACK'],
                  'cure_red' : all_events['CURE_RED'],
                  'builed_research_station' : all_events['BUILED_RESEARCH_STATION'],
                  'switch_bord_to_cards' : all_events['SWITCH_BORD_TO_CARDS'],
                  'player 1' : all_events['PLAYER_1'],
                  'player 2' : all_events['PLAYER_2'],
                  'player 3' : all_events['PLAYER_3'],
                  'player 4' : all_events['PLAYER_4'],
                  'use_event_card' : all_events['USE_EVENT_CARD'],
                  'apply_forcast' : all_events['APPLY_FORECAST'],
                  'apply_resilient_population' : all_events['APPLY_RESILIENT_POPULATION'],
                  'contingency_planner_take_discard_card' : all_events['CONTINGENCY_PLANNER_TAKE_DISCARD_CARD']}

events_cards_events = {'one quiet night' : all_events['ONE_QUIET_NIGHT'],
                       'resilient population' : all_events['RESILIENT_POPULATION'],
                       'forecast' : all_events['FORECAST'],
                       'airlift' : all_events['AIRLIFT'],
                       'government grant' : all_events['GOVERNMENT_GRANT']}

def handel_event(event, cities, cycle_player, corent_player, bord_state, players, all_bottons, player_input):
    my_bottons = all_bottons[player_input['corent_page']]
    if player_input['corent_page'] == 'map':
        player_input['chosen_city'] = bord_map.clicked_on_city(cities, corent_player, bord_state, player_input['chosen_city'], event, player_input['unlimited_movement'], player_input['picked_player'], players)
        if player_input['chosen_city']: player_input['unlimited_movement'] = False
        if player_input['chosen_city']: player_input['active_event'] = False

        bord_state.infaction_discard_cards[-1].handle_discard_event(event)
        if bord_state.player_discard_cards: bord_state.player_discard_cards[-1].handle_discard_event(event, corent_player)

    elif player_input['corent_page'] == 'cards':
        for player in players:
            
            if player.role == 'Contingency_Planner':
                if player.contingency_planner_event_card: 
                    player_input['chosen_card'] = player.contingency_planner_event_card.handle_event(event, player_input['chosen_card']) 

            for card in player.hand:
                player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    elif player_input['corent_page'] == 'forecast':
        for card in bord_state.infaction_cards[:6]:
            player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])

    elif player_input['corent_page'] == 'resilient_population':
        for card in bord_state.infaction_discard_cards:
            player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])
       
    elif player_input['corent_page'] == 'operation_expert_discard_events_cards':
        discard_event_cards = [card for card in bord_state.player_discard_cards if type(card) == data.EventCard]
        for card in discard_event_cards:
            player_input['chosen_card'] = card.handle_event(event, player_input['chosen_card'])


    for botton in my_bottons:
        botton.handle_event(event)


    if event.type == all_events['END_TURN']:
        quarantined_cities = []
        for player in players:
            if player.role == 'Quarantine_Specialist':
                quarantined_cities += player.corent_city.routes + [player.corent_city.name]
        
        quarantined_cities = set(quarantined_cities)
        draw_from_deck(bord_state, corent_player, cities, quarantined_cities)
        if not player_input['one_quiet_night']: infected_phase(bord_state, cities, quarantined_cities)
        corent_player = next(cycle_player)
        corent_player.once_per_turn = True
        corent_player.actions = ACTION_PER_TURN
        player_input['one_quiet_night'] = False


    elif event.type == all_events['CURE_BLUE']:
        treat_diseasse(bord_state, corent_player, 'BLUE')
   

    elif event.type == all_events['CURE_YELLOW']:
        treat_diseasse(bord_state, corent_player, 'YELLOW')


    elif event.type == all_events['CURE_BLACK']:
        treat_diseasse(bord_state, corent_player, 'BLACK')


    elif event.type == all_events['CURE_RED']:
        treat_diseasse(bord_state, corent_player, 'RED')


    elif event.type == all_events['SWITCH_BORD_TO_CARDS']:
        player_input['corent_page'] = 'cards'


    elif event.type == all_events['SWITCH_BORD_TO_MAP']:
        if player_input['corent_page'] == 'operation_expert_discard_events_cards': 
            player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
        
        player_input['corent_page'] = 'map'


    elif event.type == all_events['DISPLAY_INFACTION_DISCARD_CARD']:
        player_input['corent_page'] = 'infaction_discard_cards'


    elif event.type == all_events['DISPLAY_PLAYER_DISCARD_CARD']:
        player_input['corent_page'] = 'discard_player_cards'


    elif event.type == all_events['DISPLAY_CONTINGENCY_PLANNER_DISCARD_CARD']:
        player_input['corent_page'] = 'operation_expert_discard_events_cards'


    elif event.type == all_events['BUILED_RESEARCH_STATION']:
        government_grant = player_input['government_grant']
        chosen_city = player_input['chosen_city']
        if len(player_input['picked_cards']) == 1: 
            picked_card = player_input['picked_cards'][0]
        
        else:
            picked_card = None

        builed_research_station(bord_state, corent_player, cities, government_grant, city_card=picked_card, builed_city=chosen_city)
        player_input['government_grant'] = False
        player_input['chosen_city'] = None
        player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])


    elif event.type == all_events['SHARE_KNOWLEDGE']:
        if not player_input['active_event']:    
            picked_player = player_input['picked_player']
            picked_cards = player_input['picked_cards']
            share_knowledge(corent_player, picked_player, picked_cards)
            player_input['picked_cards'] = reset_picked_cards(picked_cards)
            player_input['picked_player'] = None


    elif event.type == all_events['DISCOVER_CURE']:
        if not player_input['active_event']:    
            picked_cards = player_input['picked_cards']
            discover_cure(bord_state, picked_cards, corent_player)
            for player in players:
                if player.role == 'Medic':
                    clear_discovered_cure_diseasse(bord_state, player)

            player_input['picked_cards'] = reset_picked_cards(picked_cards)


    elif event.type == all_events['DIRECT_FLIGHT']:
        if not player_input['active_event']:
            picked_cards = player_input['picked_cards']
            picked_player = player_input['picked_player']
            player_input['unlimited_movement'] = direct_flight(bord_state, corent_player, picked_cards, cities, picked_player)
            player_input['picked_cards'] = reset_picked_cards(picked_cards)
            if not player_input['unlimited_movement']: player_input['picked_player'] = None
        

    elif event.type == all_events['CLICK_ON_CARD']:
        player_input = pick_or_unpick_a_card(player_input)


    elif event.type == all_events['CLICK_ON_CITY']:
        if player_input['government_grant']:
            pygame.event.post(pygame.event.Event(all_events['BUILED_RESEARCH_STATION']))
            
        else:
            pygame.event.post(pygame.event.Event(all_events['MOVE_TO_CITY']))


    elif event.type == all_events['MOVE_TO_CITY']:
        airlift = player_input['airlift']
        picked_player = player_input['picked_player']
        chosen_city = player_input['chosen_city']
        move_to_city(bord_state, chosen_city, corent_player, airlift, picked_player)
        player_input['chosen_city'] = None
        player_input['airlift'] = False
        player_input['picked_player'] = None


    elif event.type == all_events['PLAYER_1']:
        player_input['picked_player'] = players[0]
    

    elif event.type == all_events['PLAYER_2']:
        player_input['picked_player'] = players[1]
    

    elif event.type == all_events['PLAYER_3']:
        player_input['picked_player'] = players[2]
    

    elif event.type == all_events['PLAYER_4']:
        player_input['picked_player'] = players[3]


    elif event.type == all_events['USE_EVENT_CARD']:
        if not player_input['active_event'] and len(player_input['picked_cards']) == 1:
            event_card = player_input['picked_cards'][0]
            if type(event_card) == data.EventCard:
                for player in players:
                    if event_card == player.contingency_planner_event_card:
                        player.contingency_planner_event_card = None
                
                else:    
                    discard_card(players, event_card, bord_state)
                
                event_card.use_event_card() 

        player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])


    elif event.type == all_events['ONE_QUIET_NIGHT']:
        player_input['one_quiet_night'] = True


    elif event.type == all_events['RESILIENT_POPULATION']:
        player_input['corent_page'] = 'resilient_population'
        player_input['active_event'] = True


    elif event.type == all_events['APPLY_RESILIENT_POPULATION']:
        if len(player_input['picked_cards']) == 1:
            for i, card in enumerate(bord_state.infaction_discard_cards):
                if card == player_input['picked_cards'][0]:
                    bord_state.infaction_discard_cards.pop(i)
                    player_input['corent_page'] = 'map'
                    player_input['active_event'] = False


    elif event.type == all_events['FORECAST']:
        player_input['corent_page'] = 'forecast'


    elif event.type == all_events['APPLY_FORECAST']:
        if len(player_input['picked_cards']) == 6:
            bord_state.infaction_cards = player_input['picked_cards'] + bord_state.infaction_cards[6:]
            player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])
            player_input['corent_page'] = 'map'


    elif event.type == all_events['AIRLIFT']:
        player_input['unlimited_movement'] = True
        player_input['airlift'] = True
        player_input['corent_page'] = 'map'
        player_input['active_event'] = True


    elif event.type == all_events['GOVERNMENT_GRANT']:
        player_input['active_event'] = True
        player_input['government_grant'] = True
        player_input['unlimited_movement'] = True
        player_input['corent_page'] = 'map'


    elif event.type == all_events['CONTINGENCY_PLANNER_TAKE_DISCARD_CARD']:    
        if (len(player_input['picked_cards']) == 1 and
            corent_player.role == 'Contingency_Planner'):

            contingency_planner_take_event_card(corent_player, player_input['picked_cards'], bord_state)
            player_input['corent_page'] = 'map'

        player_input['picked_cards'] = reset_picked_cards(player_input['picked_cards'])

 

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