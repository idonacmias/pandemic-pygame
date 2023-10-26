from display import city, card, tokens, player
from .color import colors_palette

def draw_bord(screen, font, corent_page, cities, players, bord_state, my_bottons):
   corent_botton = my_bottons[corent_page]
   if corent_page == 'map':
      draw_map(screen, font, cities, players, bord_state, corent_botton)

   elif corent_page == 'cards':
      draw_cards(screen, font, cities, players, bord_state, corent_botton)

   elif corent_page == 'forecast':
      draw_forcast(screen, font, bord_state, corent_botton)

   elif corent_page == 'resilient_population':
      draw_infaction_discard_cards(screen, font, bord_state, corent_botton)

   elif corent_page == 'infaction_discard_cards':
      draw_infaction_discard_cards(screen, font, bord_state, corent_botton)

   elif corent_page == 'discard_player_cards':
      draw_discard_player_cards(screen, font, bord_state, corent_botton)

def draw_map(screen, font, cities, players, bord_state, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   draw_cities(screen, font, cities)    
   card.display_back_infaction_card(screen)
   card.display_back_players_card(screen)
   card.display_infaction_discard_card(screen, font, bord_state)
   card.display_player_discard_card(screen, font, bord_state)
   tokens.draw_infaction_rate(screen, font, bord_state)
   tokens.draw_outbreak_bar(screen, font, bord_state.outbreack)
   tokens.draw_medicen_bar(screen, bord_state.cure)
   player.draw(cities, screen, players)
   for botton in corent_botton:
      botton.draw(screen, font)

   
def draw_cities(screen, font, cities):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, font)


def draw_cards(screen, font, cities, players, bord_state, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   card.dispaly_players_cards(screen, font, players)
   for botton in corent_botton:
      botton.draw(screen, font)
   
   tokens.draw_medicen_bar(screen, bord_state.cure)


def draw_forcast(screen, font, bord_state, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   for botton in corent_botton:
      botton.draw(screen, font)
   
   card.draw_list_of_cards(screen, font, bord_state.infaction_cards[:6])


def draw_infaction_discard_cards(screen, font, bord_state, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   for botton in corent_botton:
      botton.draw(screen, font)
   
   card.draw_list_of_cards(screen, font, bord_state.infaction_discard_cards)


def draw_discard_player_cards(screen, font, bord_state, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   for botton in corent_botton:
      botton.draw(screen, font)
   
   card.draw_list_of_cards(screen, font, bord_state.player_discard_cards)
