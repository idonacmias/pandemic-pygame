from display import colors_palet, city, card, tokens, player, bottons, bord

def draw_bord(screen, font, corent_page, cities, players):
   if corent_page == 'map':
      draw_map(screen, font, cities, players)

   if corent_page == 'cards':
      draw_cards(screen, font, cities, players)

def draw_map(screen, font, cities, players):
   screen.fill(colors_palet['PURPLE'])
   draw_cities(screen, font, cities)    
   card.display_back_infaction_card(screen)
   card.dispaly_front_infaction_card(screen, cities['Lagos'], font)
   card.display_back_players_card(screen)
   card.dispaly_front_player_card(screen, cities['Lagos'], font)
   tokens.draw_infaction_scale(screen, font, 0)
   tokens.draw_outbreak_bar(screen, font, 0)
   tokens.draw_medicen_bar(screen)
   player.draw(cities, screen, players)
   bottons.draw(screen, font)

def draw_cities(screen, font, cities):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, font)

def draw_cards(screen, font, cities, players):
   screen.fill(colors_palet['PURPLE'])
   card.dispaly_player_cards(screen, font, cities, players)
