from .color import colors_palette
from .drop_selects import remove_player, add_player
import pygame



def draw_manues(screen, font, clock, player_input, all_bottons, all_labels, drop_selects, color_picker):
   corent_page = player_input['corent_page']
   corent_botton = all_bottons[corent_page]
   corent_labels = all_labels[corent_page] if corent_page in all_labels.keys() else []
   corent_drop_select = drop_selects[corent_page] if corent_page in drop_selects.keys() else []
   if corent_page == 'costum_game': 
      corent_labels[0].text = str(player_input['num_of_epidemic'])
      if len(drop_selects[corent_page]) > player_input['num_players']:
         drop_selects[corent_page] = remove_player(drop_selects[corent_page])

      elif len(drop_selects[corent_page]) < player_input['num_players']:
         drop_selects[corent_page] = add_player(drop_selects[corent_page])

   draw_manue(screen, font, corent_botton, corent_labels, corent_drop_select)
   if corent_page == 'color_setting': draw_color_setting(screen, font, color_picker)
   pygame.display.update()


def draw_manue(screen, font, corent_botton, corent_labels, corent_drop_select):
   screen.fill(colors_palette['PURPLE'])
   for botton in corent_botton:
      botton.draw(screen, font)

   for label in corent_labels:
      label.draw(screen, font)


   for drop_select in corent_drop_select:
      drop_select.draw(screen, font)


def draw_color_setting(screen, font, color_picker):
   color_picker.draw(screen)
   