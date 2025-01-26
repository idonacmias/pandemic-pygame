from .event import all_events
import pygame
import sys
# from display import costum_game_drop_select 




def handel_manue_event(event, all_bottons, player_input, drop_selects, color_picker):
    handel_bottons_events(event, all_bottons, player_input['corent_page'])
    handel_drop_selects_events(event, drop_selects, player_input['corent_page'])
    color_picker.update()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

        
    elif event.type == all_events['NEW_GAME']:
        player_input['new_game'] = True
        player_input['corent_page'] = 'map'

    elif event.type == all_events['SWITCH_BORD_TO_MAIN_MANUE']:
        player_input['corent_page'] = 'main_manue'


    elif event.type == all_events['SWITCH_BORD_TO_COSTUM_GAME']:
        player_input['corent_page'] = 'costum_game'

    elif event.type == all_events['SWITCH_BORD_TO_SETTING']:
        player_input['corent_page'] = 'setting'

    elif event.type == all_events['SWITCH_BORD_TO_COLOR_SETTING']:
        player_input['corent_page'] = 'color_setting'

    elif event.type == all_events['ADD_EPIDEMIC_CARD']:
        if player_input['num_of_epidemic'] != 6: player_input['num_of_epidemic'] += 1
    
    elif event.type == all_events['SUBTRACT_EPIDEMIC_CARD']:
        if player_input['num_of_epidemic'] != 4: player_input['num_of_epidemic'] -= 1 

    elif event.type == all_events['ADD_PLAYER']:
        if player_input['num_players'] < 4: player_input['num_players'] += 1 
        # drop_select['costum_game'].append(costum_game_drop_select(player_input['num_players']))

    elif event.type == all_events['SUBTRACT_PLAYER']:
        if player_input['num_players'] > 2: player_input['num_players'] -= 1 

    return player_input

def handel_bottons_events(event, all_bottons, corent_page):
    my_bottons = all_bottons[corent_page]    
    for botton in my_bottons:
        botton.handel_event(event)

def handel_drop_selects_events(event, drop_selects, corent_page):
    corent_drop_select = drop_selects[corent_page] if corent_page in drop_selects.keys() else []
    for drop_select in corent_drop_select:
        drop_select.handel_event(event)
