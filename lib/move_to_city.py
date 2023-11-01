from .diseasse import treat_diseasse
from display import Color 

def move_to_city(bord_state, chosen_city, corent_player, airlift, picked_player):
    if ((airlift or 
        corent_player.role == 'Dispatcher')and
        picked_player): 
    
        player = picked_player 

    else:
        player=corent_player

    player.corent_city = chosen_city
    if player.role == 'Medic': 
        clear_discovered_cure_diseasse(bord_state, player)
        
    if not airlift: corent_player.use_action()


def clear_discovered_cure_diseasse(bord_state, player):
    for color in Color:
        color_name = color.name
        if bord_state.cure[color_name] > 0:
            treat_diseasse(bord_state, player, color_name, action=False)
