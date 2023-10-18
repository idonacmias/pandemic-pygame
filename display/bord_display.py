from display import city, card, tokens, player
from .color import colors_palet
from .constances import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS, MAP_SMALL_BUTTONS_POINTS, MAP_SMALL_BUTTONS_TEXTS, BUTTON_HIGHT, BUTTON_WHIDTH, SMALL_BUTTON_WHIDTH, SMALL_BUTTON_HIGHT

def draw_bord(screen, font, corent_page, cities, players, bord_state, my_bottons):
   corent_botton = my_bottons[corent_page]
   if corent_page == 'map':
      draw_map(screen, font, cities, players, bord_state, corent_botton)

   if corent_page == 'cards':
      draw_cards(screen, font, cities, players, bord_state, corent_botton)

def draw_map(screen, font, cities, players, bord_state, my_botton):
   screen.fill(colors_palet['PURPLE'])
   draw_cities(screen, font, cities)    
   card.display_back_infaction_card(screen)
   card.display_back_players_card(screen)
   card.display_infaction_discard_card(screen, font, bord_state)
   card.display_player_discard_card(screen, font, bord_state)
   tokens.draw_infaction_rate(screen, font, bord_state)
   tokens.draw_outbreak_bar(screen, font, bord_state.outbreack)
   tokens.draw_medicen_bar(screen, bord_state.cure)
   player.draw(cities, screen, players)
   for botton in my_botton:
      botton.draw(screen, font)
   
def draw_cities(screen, font, cities):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, font)


def draw_cards(screen, font, cities, players, bord_state, my_botton):
   screen.fill(colors_palet['PURPLE'])
   card.dispaly_players_cards(screen, font, players)
   for botton in my_botton:
      botton.draw(screen, font)
   
   tokens.draw_medicen_bar(screen, bord_state.cure)
