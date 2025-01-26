import pygame
from itertools import cycle
from data import Player, crate_cities, FIRST_CITY, BordState, NUM_PLAYERS_CARDS
from events import handel_event, handel_manue_event, all_events
from display import bord_display, manue_display ,all_bottons, all_labels, drop_selects, color_pickers
from lib import first_infaction

def main():
    pygame.init()
    screen = pygame.display.set_mode()
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
    player_input = create_player_input()
    manues = ['main_manue', 'costum_game', 'setting', 'win', 'lose', 'color_setting']


    while True:
        if player_input['corent_page'] in manues:
            player_input = run_manues(screen, font, clock, player_input, all_bottons, all_labels, drop_selects, color_pickers)
        
        elif player_input['new_game']:
            players, bord_state, cities, cycle_player, player_input = new_game(player_input, drop_selects['costum_game'])
            player_input['new_game'] = False

        else:
            player_input = run_game(screen, font, player_input, cities, players, bord_state, all_bottons, clock, cycle_player, all_labels)
        clock.tick(60)


def new_game(player_input, costum_players):
    num_players = player_input['num_players']
    cities = crate_cities()
    bord_state = BordState(cities)
    first_city = cities[FIRST_CITY]
    first_city.research_station = True
    players_cards = first_draw_player_cards(bord_state, num_players)
    players = [Player(players_cards[i], first_city, role=drop_select.chosen_option) for i, drop_select in enumerate(costum_players)]
    first_infaction(bord_state, cities)
    bord_state.insert_epidemic(player_input['num_of_epidemic'])
    cycle_player = cycle(players)
    player_input['corent_player'] = next(cycle_player)
    return players, bord_state, cities, cycle_player, player_input  


def first_draw_player_cards(bord_state, num_players):
    num_players_cards = NUM_PLAYERS_CARDS[num_players - 2]
    player_cards = []
    for _ in range(num_players):
        player_cards.append(bord_state.players_deck[:num_players_cards])
        bord_state.players_deck = bord_state.players_deck[num_players_cards:]

    return player_cards

    
def create_player_input():
    player_input = {'corent_page' : 'main_manue',
                'corent_player' : None,
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
                'dubel_epidemic' : False,
                'new_game' : False,
                'num_players' : 2,
                'num_of_epidemic' : 4}

    return player_input

def run_manues(screen, font, clock, player_input, all_bottons, label, drop_selects, color_pickers):
    manue_display.draw_manues(screen, font, clock, player_input, all_bottons, label, drop_selects, color_pickers)
    for event in pygame.event.get():
        player_input = handel_manue_event(event, all_bottons, player_input, drop_selects, color_pickers)
    
    return player_input

def run_game(screen, font, player_input, cities, players, bord_state, all_bottons, clock, cycle_player, all_labels):
    bord_display.draw_bord(screen, font, player_input['corent_page'], cities, players, bord_state, all_bottons, player_input['corent_player'], player_input['picked_player'], all_labels)
    if is_lose(bord_state):
        player_input['corent_page'] = 'lose'
         
    elif is_won(bord_state):
        player_input['corent_page'] = 'win'

    for event in pygame.event.get():
        player_input = handel_event(event, cities, cycle_player, bord_state, players, all_bottons, player_input)

    return player_input


def is_lose(bord_state):
    return (bord_state.outbreack >= 8 or
            not bord_state.players_deck or #if ocerd may crash the game do to player_input['end_turn_sequence'] = None
            is_disease_cube_empty(bord_state.disease_cube))

def is_disease_cube_empty(disease_cube):
    for disease in disease_cube:
        if disease < 0:
            return True


def is_won(bord_state):
    if list(bord_state.cure.values()).count(0) == 0:
        return True



if __name__ == '__main__':
    main()