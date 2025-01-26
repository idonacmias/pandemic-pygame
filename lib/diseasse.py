from display import Color 


def treat_diseasse(bord_state, corent_player, color_name, cities, action=True):
    corent_city = corent_player.corent_city
    color = Color.__members__[color_name] - 1 
    if is_diseasse_in_city(corent_city, color_name):
        if action: corent_player.use_action()

        if bord_state.cure[color_name] == 1 or corent_player.role == 'Medic':
            new_cube_in_city = 0

        else:
            new_cube_in_city = corent_city.diseasse_cubes[color_name] - 1

        bord_state.disease_cube[color] += corent_city.diseasse_cubes[color_name] - new_cube_in_city
        corent_city.diseasse_cubes[color_name] = new_cube_in_city
        try_eradication(cities, color_name, bord_state)

def is_diseasse_in_city(corent_city, color_name):
    if corent_city.diseasse_cubes[color_name] != 0:
        return True


def try_eradication(cities, color_name, bord_state):
    if is_diseasse_eradicate(cities, color_name, bord_state):
            bord_state.cure[color_name] = 2

def is_diseasse_eradicate(cities, color_name, bord_state):
    if (is_cities_clean_from_dissease(cities, color_name) and
        is_cure_discoverd(bord_state, color_name)):

        return True


def is_cities_clean_from_dissease(cities, color_name):
    for city in cities.values():
        if city.diseasse_cubes[color_name] > 0:
            break
    
    else: 
        return True


def is_cure_discoverd(bord_state, color_name):
    if bord_state.cure[color_name] == 1:
        return True

