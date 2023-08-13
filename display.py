import pygame
import sys

from display import colors_palet, card, tokens, city, CITY_RADIUS

from cities import cities

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
    card.display_back_infaction_card(screen)
    card.dispaly_front_infaction_card(screen, cities['Lagos'], font)
    card.display_back_players_card(screen)
    card.dispaly_front_player_card(screen, cities['Lagos'], font)
    tokens.draw_infaction_scale(screen, font, 0)
    tokens.draw_outbreak_bar(screen, font, 0)

    tokens.draw_medicen_bar(screen)

    FIRST_CITY = 'Atlanta'
    corent_city = cities[FIRST_CITY]
    corent_city.resarch_station = True
    city.draw(corent_city, screen, colors_palet['PINK'], font)
    return corent_city

def draw_cities(screen, font):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, colors_palet[city_data.color.name], font)
    
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
            city_data = cities[city_name]
            temp_min_radius = city.click_lenth_from_center(city_data, muose_point)
            if temp_min_radius <= min_radius:
                min_radius = temp_min_radius
                closest_city = city_data


        if closest_city:
            city.draw(closest_city, screen, colors_palet['PINK'], font)
            city.draw(corent_city, screen, colors_palet[corent_city.color.name], font)
            return closest_city 

    return corent_city

if __name__ == '__main__':
    main(cities)