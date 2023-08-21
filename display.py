import pygame
import sys

from display import colors_palet, card, tokens, city, CITY_RADIUS, player, bottons
from constances import FIRST_CITY
from cities import cities
from Player import Player


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
        city.draw(city_data, screen, colors_palet[city_data.color.name], font)
    
def if_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def clicked_on_city(event, screen, font, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        min_radius = CITY_RADIUS
        closest_city = None
        corent_city = cities[players[corent_player].corent_city]
        for city_name in corent_city.routes:
            city_data = cities[city_name]
            temp_min_radius = city.click_lenth_from_center(city_data, mouse_point)
            if temp_min_radius <= min_radius:
                min_radius = temp_min_radius
                closest_city = city_data.name


        if closest_city:
            players[0].corent_city = closest_city
            city.draw(corent_city, screen, colors_palet[corent_city.color.name], font)
            player.draw(cities, screen, players)

def click_on_botton(event, screen, font, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        botton_clicked = bottons.witch_click_on(mouse_point)

        if botton_clicked == 'display player cards':
            card.dispaly_player_cards(screen, font, cities, players)
        
        elif botton_clicked == 'discover cure':
            print('cure discoverd')

        elif botton_clicked == 'builed reserch station':
            corent_city = cities[players[corent_player].corent_city]
            corent_city.resarch_station = True
            city.draw(corent_city, screen, colors_palet[corent_city.color.name], font)
            player.draw(cities, screen, players)




if __name__ == '__main__':
    main(cities)