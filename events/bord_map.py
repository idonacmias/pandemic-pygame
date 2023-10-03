from display import card, CITY_RADIUS, bottons
from display import MAP_BUTTONS_POINTS,MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT
from lib import treat_diseasse, builed_research_station

def clicked_on_city(cities, corent_player, mouse_point, bord_state):
    min_radius = CITY_RADIUS
    closest_city = None
    routes = get_routes(cities, corent_player, bord_state)
    for city_name in routes:
        city = cities[city_name]
        temp_min_radius = click_lenth_from_center(city, mouse_point)
        if temp_min_radius <= min_radius:
            min_radius = temp_min_radius
            closest_city = city

    if closest_city: move_player_to_city(corent_player, closest_city)


def get_routes(cities, corent_player, bord_state):
    corent_city = corent_player.corent_city
    routes = corent_city.routes.copy()
    if corent_city.research_station:
        routes += get_reserch_station_cities(bord_state, corent_city) 

    return routes

def get_reserch_station_cities(bord_state, corent_city):
    research_stations_cities = bord_state.research_stations.copy()
    for i, city_name in enumerate(research_stations_cities):
        if corent_city.name == city_name:
            research_stations_cities.pop(i)

    return research_stations_cities 
    
def click_lenth_from_center(city, mouse_point):
    return abs(city.point[0] - mouse_point[0]) + abs(city.point[1] - mouse_point[1])


def move_player_to_city(corent_player, closest_city):
    corent_player.corent_city = closest_city
    corent_player.actions -= 1


def click_on_botton(cities, corent_player, botton_clicked, bord_state):
    print(botton_clicked)
    if botton_clicked == 'display player cards': return 'cards'

    elif botton_clicked == 'builed research station':
        builed_research_station(bord_state, corent_player, cities)

    elif botton_clicked in ['blue', 'yellow', 'black', 'red']:
        color_name = botton_clicked.upper()
        treat_diseasse(bord_state, corent_player, color_name)
