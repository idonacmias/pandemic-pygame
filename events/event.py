import pygame
from display import CITY_RADIUS
from display import colors_palet, card, tokens, city, CITY_RADIUS, player, bottons

def clicked_on_city(event, screen, font, cities, players, corent_player):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_point = pygame.mouse.get_pos()
        min_radius = CITY_RADIUS
        closest_city_name = None
        corent_city = cities[players[corent_player].corent_city_name]
        for city_name in corent_city.routes:
            city_data = cities[city_name]
            temp_min_radius = city.click_lenth_from_center(city_data, mouse_point)
            if temp_min_radius <= min_radius:
                min_radius = temp_min_radius
                closest_city_name = city_data.name


        if closest_city_name:
            players[0].corent_city_name = closest_city_name
            city.draw(corent_city, screen, font)
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
            corent_city = cities[players[corent_player].corent_city_name]
            corent_city.resarch_station = True
            city.draw(corent_city, screen, font)
            player.draw(cities, screen, players)

