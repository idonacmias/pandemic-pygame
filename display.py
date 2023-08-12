import pygame
import sys

from color import colors_palet
from cities import cities   
import card
import tokens

from constances import EDGE_CITIES, CITY_RADIUS, INFACTION_CARDS_POSITION, DISCARD_INFACTION_CARDS_POSITION, PLAYERS_CARDS_POSITION, DISCARD_PLAYERS_CARDS_POSITION, CARD_HALF_WHIDTH, CARD_HALF_HIGHT



def main(cities):
    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill(colors_palet['PURPLE'])
    font = pygame.font.Font(None, 28) 
    clock = pygame.time.Clock()
    corent_city = set_bord(screen, font)
    while True:
        for event in pygame.event.get():
            if_quit(event)
            corent_city = clicked_on_city(event, cities, screen, corent_city, font)

        pygame.display.update()
        clock.tick(60)

def set_bord(screen, font):
    draw_cities(screen, font)    
    card.display_back_infaction_card(screen, INFACTION_CARDS_POSITION)
    card.dispaly_front_infaction_card(screen, DISCARD_INFACTION_CARDS_POSITION, cities['Lagos'], font)
    card.display_back_players_card(screen, PLAYERS_CARDS_POSITION)
    card.dispaly_front_player_card(screen, DISCARD_PLAYERS_CARDS_POSITION, cities['Lagos'], font)
    tokens.draw_infaction_scale(screen, font, 0)
    tokens.draw_outbreak_bar(screen, font, 0)

    tokens.draw_medicen_bar(screen)

    FIRST_CITY = 'Atlanta'
    corent_city = cities[FIRST_CITY]
    corent_city.resarch_station = True
    corent_city.draw(screen, colors_palet['PINK'], font)
    return corent_city

def draw_cities(screen, font):
    for city in cities.values():
        city.conect_routes(screen, cities, font)

    for city in cities.values():
        city.draw(screen, colors_palet[city.color.name], font)
    
def if_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def clicked_on_city(event, cities, screen, corent_city, font):
    if event.type == pygame.MOUSEBUTTONUP:
        muose_point = pygame.mouse.get_pos()
        min_radius = CITY_RADIUS
        closest_city = None

        for city_name in corent_city.routes:
            city = cities[city_name]
            temp_min_radius = city.click_lenth_from_center(muose_point)
            if temp_min_radius <= min_radius:
                min_radius = temp_min_radius
                closest_city = city


        if closest_city:
            closest_city.draw(screen, colors_palet['PINK'], font)
            corent_city.draw(screen, colors_palet[corent_city.color.name], font)
            return closest_city 

    return corent_city

if __name__ == '__main__':
    main(cities)