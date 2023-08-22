import pygame
from data import Player, cities, FIRST_CITY
from events import if_quit, clicked_on_city, click_on_botton
from display import colors_palet, bord


def main():
    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill(colors_palet['PURPLE'])
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
    players = set_bord(screen, font, 4)
    corent_player = 0
    while True:
        for event in pygame.event.get():
            if_quit(event)
            clicked_on_city(event, screen, font, cities, players, corent_player)
            click_on_botton(event, screen,font, cities, players, corent_player)

        pygame.display.update()
        clock.tick(60)

def set_bord(screen, font, num_players=2):
    cities[FIRST_CITY].resarch_station = True
    PLAYER_COLORS = ['GREEN', 'PURPLE', 'GRAY', 'PINK']
    players = [Player(PLAYER_COLORS[i]) for i in range(num_players)]
    bord.draw_bord(screen, font, cities, players)
    return players



if __name__ == '__main__':
    main()