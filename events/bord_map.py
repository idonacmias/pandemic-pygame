def clicked_on_city(cities, corent_player, bord_state, chosen_city, event, unlimited_movement, picked_player, players):
    routes = []
    if corent_player.role == 'Dispatcher':
        if picked_player: 
            moving_player = picked_player 
        
        else: 
            moving_player = corent_player
        
        routes += [player.corent_city.name for player in players if player.corent_city != moving_player.corent_city] 
        
    else:
        moving_player = corent_player

    routes += get_routes(cities, moving_player, bord_state, unlimited_movement)
    print(set(routes))
    for city_name in set(routes):
        city = cities[city_name]
        chosen_city = city.handle_event(event, chosen_city)

    return chosen_city


def get_routes(cities, moving_player, bord_state, unlimited_movement):
    if unlimited_movement: routes = [city.name for city in cities.values()]
    
    else:
        corent_city = moving_player.corent_city
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
