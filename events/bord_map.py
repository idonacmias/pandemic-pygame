from display import card, CITY_RADIUS, bottons
from display import MAP_BUTTONS_POINTS,MAP_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT


def clicked_on_city(cities, corent_player, mouse_point, bord_state):
    min_radius = CITY_RADIUS
    closest_city = None
    routes = get_routes(cities, corent_player, bord_state)
    for city_name in routes:
        city_data = cities[city_name]
        temp_min_radius = click_lenth_from_center(city_data, mouse_point)
        if temp_min_radius <= min_radius:
            min_radius = temp_min_radius
            closest_city = city_data

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
    if botton_clicked == 'display player cards': return 'cards'

    elif botton_clicked == 'discover cure': print('cure discoverd')

    elif botton_clicked == 'builed research station':
        click_builed_research_station(bord_state, corent_player, cities)

    elif botton_clicked == 'cure diseasse': 
        click_cure_diseasse(bord_state, cities, corent_player)        


def click_builed_research_station(bord_state, corent_player, cities):
    corent_city = corent_player.corent_city
    if not corent_city.research_station: 
        corent_player.actions -= 1
        add_city_research_station(bord_state, corent_city, cities)

def add_city_research_station(bord_state, city, cities):
    if bord_state.num_research_station <= 0: remove_city_research_station(bord_state, cities) 
    city.research_station = True
    bord_state.research_stations.append(city.name)
    bord_state.num_research_station -= 1
        
def remove_city_research_station(bord_state, cities, research_station_cuonter=0):
    research_station_name = bord_state.research_stations.pop(research_station_cuonter)
    cities[research_station_name].research_station = False
    bord_state.num_research_station += 1


def click_cure_diseasse(bord_state, cities, corent_player):
    print('cure diseasse')
    corent_city = corent_player.corent_city
    if corent_city.diseasse_cubes :
        print('cure me!')