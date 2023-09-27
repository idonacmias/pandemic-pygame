import pygame
import sys
from data import Player, cities, FIRST_CITY, EventCard, BordState, ACTION_PER_TURN, NUM_PLAYERS_CARDS
from events import handel_event
from display import colors_palet, bord_display
from itertools import cycle
from lib import first_infaction, infected_phase, draw_from_deack

def main():
    pygame.init()
    # screen_info = pygame.display.Info()
    # print(screen_info)
    screen = pygame.display.set_mode()
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
    
    players, bord_state = set_bord(4)

    cycle_player = cycle(players)
    corent_player = next(cycle_player)
    
    corent_page = 'map'
    piked_cards = []


    while True:
        # screen_info = pygame.display.Info()
        # print(screen_info)
        
        if corent_player.actions == 0: 
            print('END_TURN')
            draw_from_deack(bord_state, corent_player)
            infected_phase(bord_state)
            corent_player = next(cycle_player)
            corent_player.actions = ACTION_PER_TURN

        for event in pygame.event.get():
            if_quit(event)
           
            temp_page, piked_cards = handel_event(event, corent_page, cities, players, corent_player, bord_state, piked_cards)

            if temp_page:
                corent_page = temp_page

        bord_display.draw_bord(screen, font, corent_page, cities, players, bord_state)
        pygame.display.update()
        clock.tick(60)


def if_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def set_bord(num_players=2):
    bord_state = BordState()
    first_city = cities[FIRST_CITY]
    first_city.research_station = True
    PLAYER_COLORS = ['GREEN', 'PURPLE', 'GRAY', 'PINK']
    players_cards = first_draw_player_cards(bord_state, num_players)
    players = [Player(PLAYER_COLORS[i], players_cards[i], first_city) for i in range(num_players)]
    first_infaction(bord_state)
    bord_state.insert_epidemic()
    return players, bord_state


def first_draw_player_cards(bord_state, num_players):
    num_players_cards = NUM_PLAYERS_CARDS[num_players - 2]
    player_cards = []
    for _ in range(num_players):
        player_cards.append(bord_state.players_deck[:num_players_cards])
        bord_state.players_deck = bord_state.players_deck[num_players_cards:]

    return player_cards
    

if __name__ == '__main__':
    main()