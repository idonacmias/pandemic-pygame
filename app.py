import pygame
import sys
from data import Player, cities, FIRST_CITY, EventCard, BordState
from events import handel_event, END_TURN
from display import colors_palet, bord_display
from itertools import cycle


def main():
    pygame.init()
    # screen_info = pygame.display.Info()
    # print(screen_info)
    screen = pygame.display.set_mode()
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
    
    players, bord_state = set_bord(4)
    
    corent_page = 'map'
    cycle_player = cycle(players)
    corent_player = next(cycle_player)
    
    one_quiet_night = EventCard('one quiet night', 'skip next infaction phase')
    player_discard = one_quiet_night


    while True:
        # screen_info = pygame.display.Info()
        # print(screen_info)
        if corent_player.actions == 0:
            pygame.event.post(pygame.event.Event(END_TURN))
            corent_player = next(cycle_player)
            


        for event in pygame.event.get():
            if_quit(event)
            temp_page = handel_event(event, corent_page, cities, players, corent_player, cycle_player, bord_state)

            if temp_page:
                corent_page = temp_page

        bord_display.draw_bord(screen, font, corent_page, cities, players, player_discard, bord_state)
        pygame.display.update()
        clock.tick(60)


def if_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def set_bord(num_players=2):
    cities[FIRST_CITY].research_station = True
    PLAYER_COLORS = ['GREEN', 'PURPLE', 'GRAY', 'PINK']
    players = [Player(PLAYER_COLORS[i]) for i in range(num_players)]
    bord_state = BordState()
    return players, bord_state


if __name__ == '__main__':
    main()