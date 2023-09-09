from display import card, CITY_RADIUS, bottons
from display import MAP_BUTTONS_POINTS,MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT



def clicked_on_city(cities, players, corent_player, mouse_point):
    min_radius = CITY_RADIUS
    closest_city_name = None
    corent_city = cities[players[corent_player].corent_city_name]
    for city_name in corent_city.routes:
        city_data = cities[city_name]
        temp_min_radius = click_lenth_from_center(city_data, mouse_point)
        if temp_min_radius <= min_radius:
            min_radius = temp_min_radius
            closest_city_name = city_data.name

    if closest_city_name:
        players[corent_player].corent_city_name = closest_city_name

        
def click_lenth_from_center(city, mouse_point):
    return abs(city.point[0] - mouse_point[0]) + abs(city.point[1] - mouse_point[1])


def click_on_botton(cities, players, corent_player, botton_clicked):
    if botton_clicked == 'display player cards':
        corent_page = 'cards'
        return corent_page  

    elif botton_clicked == 'discover cure':
        print('cure discoverd')

    elif botton_clicked == 'builed reserch station':
        corent_city = cities[players[corent_player].corent_city_name]
        corent_city.resarch_station = True
