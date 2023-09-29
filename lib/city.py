from display import Color 


def builed_research_station(bord_state, corent_player, cities):
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