from display import colors_palet, city, card, tokens, player, bottons
from .constances import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS


def draw_bord(screen, font, corent_page, cities, players, player_discard, bord_state):
   if corent_page == 'map':
      draw_map(screen, font, cities, players, player_discard, bord_state)

   if corent_page == 'cards':
      draw_cards(screen, font, cities, players, bord_state)


def draw_map(screen, font, cities, players, player_discard, bord_state):
   screen.fill(colors_palet['PURPLE'])
   draw_cities(screen, font, cities)    
   card.display_back_infaction_card(screen)
   card.dispaly_front_infaction_card(screen, cities['Lagos'], font)
   card.display_back_players_card(screen)
   card.dispaly_front_player_card(screen, font, player_discard)
   tokens.draw_infaction_rate(screen, font, bord_state)
   tokens.draw_outbreak_bar(screen, font, bord_state.outbreack)
   tokens.draw_medicen_bar(screen, bord_state.cure)
   player.draw(cities, screen, players)
   buttons_data = zip(MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS)
   bottons.draw(screen, font, buttons_data)


def draw_cities(screen, font, cities):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, font)


def draw_cards(screen, font, cities, players, bord_state):
   screen.fill(colors_palet['PURPLE'])
   card.dispaly_players_cards(screen, font, cities, players)
   buttons_data = zip(CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS)
   bottons.draw(screen, font, buttons_data)
   tokens.draw_medicen_bar(screen, bord_state.cure)