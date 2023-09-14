from display import card, CITY_RADIUS, bottons
from display import MAP_BUTTONS_POINTS,MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT



def clicked_on_city(cities, corent_player, mouse_point, bord_state):
    min_radius = CITY_RADIUS
    closest_city_name = None
    corent_city = cities[corent_player.corent_city_name]
    routes = corent_city.routes.copy()
    if corent_city.research_station: routes += bord_state.research_stations

    for city_name in routes:
        city_data = cities[city_name]
        temp_min_radius = click_lenth_from_center(city_data, mouse_point)
        if temp_min_radius <= min_radius:
            min_radius = temp_min_radius
            closest_city_name = city_data.name

    if closest_city_name: move_player_to_city(corent_player, closest_city_name)

        
def click_lenth_from_center(city, mouse_point):
    return abs(city.point[0] - mouse_point[0]) + abs(city.point[1] - mouse_point[1])


def move_player_to_city(corent_player, closest_city_name):
    corent_player.corent_city_name = closest_city_name
    corent_player.actions -= 1


def click_on_botton(cities, corent_player, botton_clicked, bord_state):
    if botton_clicked == 'display player cards': return 'cards'

    elif botton_clicked == 'discover cure': print('cure discoverd')

    elif botton_clicked == 'builed research station':
        corent_city = cities[corent_player.corent_city_name]
        if corent_city.research_station: return None

        if bord_state.num_research_station <= 0: remove_city_research_station(bord_state, cities) 

        add_city_research_station(corent_city, bord_state, corent_player)

def remove_city_research_station(bord_state, cities):
    oldest_research_station = bord_state.research_stations.pop(0)
    cities[oldest_research_station].research_station = False
    bord_state.num_research_station += 1


def add_city_research_station(corent_city, bord_state, corent_player):
    corent_city.research_station = True
    bord_state.research_stations.append(corent_city.name)
    bord_state.num_research_station -= 1
    corent_player.actions -= 1
