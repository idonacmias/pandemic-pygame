import pygame

from constances import FIRST_CITY
from display import colors_palet, city, card, tokens, player, bottons
from cities import cities
from Player import Player
from events import if_quit, clicked_on_city, click_on_botton



def main(cities):
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
    draw_cities(screen, font)    
    card.display_back_infaction_card(screen)
    card.dispaly_front_infaction_card(screen, cities['Lagos'], font)
    card.display_back_players_card(screen)
    card.dispaly_front_player_card(screen, cities['Lagos'], font)
    tokens.draw_infaction_scale(screen, font, 0)
    tokens.draw_outbreak_bar(screen, font, 0)
    tokens.draw_medicen_bar(screen)
    PLAYER_COLORS = ['GREEN', 'PURPLE', 'GRAY', 'PINK']
    players = [Player(PLAYER_COLORS[i],FIRST_CITY) for i in range(num_players)]
    player.draw(cities, screen, players)
    bottons.draw(screen, font)
    return players

def draw_cities(screen, font):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, font)



if __name__ == '__main__':
    main(cities)