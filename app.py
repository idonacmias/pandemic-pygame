import pygame
from itertools import cycle
from data import Player, cities, FIRST_CITY, BordState, NUM_PLAYERS_CARDS
from events import handel_event, all_events
from display import bord_display, all_bottons
from lib import first_infaction

def main():
    pygame.init()
    screen = pygame.display.set_mode()
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
   
    players, bord_state = set_bord()
    cycle_player = cycle(players)
    player_input = {'corent_page' : 'map',
                    'corent_player' : next(cycle_player),
                    'picked_cards' : [],
                    'chosen_card' : None,
                    'picked_player' : None, 
                    'chosen_city' : None,
                    'unlimited_movement' : False,
                    'airlift' : False,
                    'government_grant' : False,
                    'one_quiet_night' : False,
                    'active_event' : False,
                    'quarantined_cities' : [],
                    'end_turn_sequence' : None,
                    'dubel_epidemic' : False}

    while True:
        bord_display.draw_bord(screen, font, player_input['corent_page'], cities, players, bord_state, all_bottons, player_input['corent_player'], player_input['picked_player'])
        clock.tick(60)
        if is_lose(bord_state):
            # print('lose')
            pass

        elif is_won(bord_state):
            # print('win')
            pass

        for event in pygame.event.get():
            player_input = handel_event(event, cities, cycle_player, bord_state, players, all_bottons, player_input)




def set_bord(num_players=2):
    bord_state = BordState()
    first_city = cities[FIRST_CITY]
    first_city.research_station = True
    players_cards = first_draw_player_cards(bord_state, num_players)
    players = [Player(players_cards[i], first_city, role='Medic') for i in range(num_players)]
    first_infaction(bord_state, cities)
    bord_state.insert_epidemic()
    return players, bord_state  


def first_draw_player_cards(bord_state, num_players):
    num_players_cards = NUM_PLAYERS_CARDS[num_players - 2]
    player_cards = []
    for _ in range(num_players):
        player_cards.append(bord_state.players_deck[:num_players_cards])
        bord_state.players_deck = bord_state.players_deck[num_players_cards:]

    return player_cards

    

def is_lose(bord_state):
    return (bord_state.outbreack >= 8 or
            not bord_state.players_deck or
            is_disease_cube_empty(bord_state.disease_cube))

def is_disease_cube_empty(disease_cube):
    for disease in disease_cube:
        if disease < 0:
            return True


def is_won(bord_state):
    cures = 0
    for cure in bord_state.cure.values():
        if cure > 0:
            cures += 1

    return cures == 4




if __name__ == '__main__':
    main()