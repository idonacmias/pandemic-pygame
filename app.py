import pygame
import sys
from data import Player, cities, FIRST_CITY, EventCard
from events import handel_event
from display import colors_palet, bord



def main():
    pygame.init()
    # screen_info = pygame.display.Info()
    # print(screen_info)
    screen = pygame.display.set_mode()
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
    corent_page = 'map'
    players = set_bord(4)
    corent_player = 0
 
    one_quiet_night = EventCard('one quiet night', 'skip next infaction phase')
    player_discard = one_quiet_night
 
    while True:
        # screen_info = pygame.display.Info()
        # print(screen_info)

        for event in pygame.event.get():
            if_quit(event)
            temp_page = handel_event(event, corent_page, cities, players, corent_player)

            if temp_page:
                corent_page = temp_page

        bord.draw_bord(screen, font, corent_page, cities, players, player_discard)
        pygame.display.update()
        clock.tick(60)


def if_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def set_bord(num_players=2):
    cities[FIRST_CITY].resarch_station = True
    PLAYER_COLORS = ['GREEN', 'PURPLE', 'GRAY', 'PINK']
    players = [Player(PLAYER_COLORS[i]) for i in range(num_players)]
    return players



if __name__ == '__main__':
    main()