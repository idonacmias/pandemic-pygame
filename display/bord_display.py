from display import city, card, tokens, player
import data
from .color import colors_palette
import pygame


def draw_bord(screen, font, corent_page, cities, players, bord_state, all_bottons, corent_player, picked_player, all_labels):
   corent_botton = all_bottons[corent_page]
   corent_labels = all_labels[corent_page] if corent_page in all_labels.keys() else []

   if (corent_page == 'map' or
      corent_page == 'map_dubel_epidemic'):
      corent_labels[0].text = f'actions left: {corent_player.actions}'
      draw_map(screen, font, cities, players, bord_state, corent_botton, corent_labels)

   elif (corent_page == 'cards' or
         corent_page == 'play_event_during_epidemic'):

      draw_players_cards_display(screen, font, cities, players, bord_state, corent_botton)

   elif corent_page == 'forecast':
      cards = bord_state.infaction_cards[:6]
      draw_cards(screen, font, cards, corent_botton)

   elif corent_page == 'resilient_population':
      cards = bord_state.infaction_discard_cards
      draw_cards(screen, font, cards, corent_botton)

   elif corent_page == 'infaction_discard_cards':
      cards = bord_state.infaction_discard_cards
      draw_cards(screen, font, cards, corent_botton)

   elif corent_page == 'discard_player_cards':
      cards = bord_state.player_discard_cards
      draw_cards(screen, font, cards, corent_botton)

   elif corent_page == 'operation_expert_discard_events_cards':
      discard_event_cards = [card for card in bord_state.player_discard_cards if type(card) == data.EventCard]
      draw_cards(screen, font, discard_event_cards, corent_botton)

   elif corent_page == 'hand_limit_end_turn':
      cards = corent_player.hand
      draw_cards(screen, font, cards, corent_botton)
   
   elif corent_page == 'hand_limit':
      cards = picked_player.hand
      draw_cards(screen, font, cards, corent_botton)
   
   pygame.display.update()


def draw_map(screen, font, cities, players, bord_state, corent_botton, corent_labels):
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
   
   for label in corent_labels:
      label.draw(screen, font)

   
def draw_cities(screen, font, cities):
    for city_data in cities.values():
        city.conect_routes(city_data, screen, cities, font)

    for city_data in cities.values():
        city.draw(city_data, screen, font)


def draw_players_cards_display(screen, font, cities, players, bord_state, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   card.dispaly_players_cards(screen, font, players)
   for botton in corent_botton:
      botton.draw(screen, font)
   
   tokens.draw_medicen_bar(screen, bord_state.cure)


def draw_cards(screen, font, cards, corent_botton):
   screen.fill(colors_palette['PURPLE'])
   for botton in corent_botton:
      botton.draw(screen, font)
   
   card.draw_list_of_cards(screen, font, cards)


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


