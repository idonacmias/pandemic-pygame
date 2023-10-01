from display import Color 


def treat_diseasse(bord_state, corent_player, color_name, action=True):
    corent_city = corent_player.corent_city
    color = Color.__members__[color_name]
    if is_diseasse_in_city(corent_city, color):
        if action: corent_player.actions -= 1

        if bord_state.cure[color_name] == 1: #TODO: PLAYER ROLL MEDIC    
            new_cube_in_city = 0

        else:
            new_cube_in_city = corent_city.diseasse_cubes[color] - 1

        corent_city.diseasse_cubes[color] = new_cube_in_city


def is_diseasse_in_city(corent_city, color):
    if corent_city.diseasse_cubes[color] != 0:
        return True