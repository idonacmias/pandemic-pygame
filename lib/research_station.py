

def builed_research_station(bord_state, corent_player, cities, action=True):
    corent_city = corent_player.corent_city
    if (not corent_city.research_station and 
        is_player_have_city_card(corent_player)):
         
        if action: corent_player.actions -= 1
        add_city_research_station(bord_state, corent_city, cities)
        remove_player_card(corent_player)

def is_player_have_city_card(corent_player):
    if corent_player.corent_city in corent_player.hand: return True

def add_city_research_station(bord_state, city, cities):
    if bord_state.num_research_station <= 0: remove_city_research_station(bord_state, cities) 
    city.research_station = True
    bord_state.research_stations.append(city.name)
    bord_state.num_research_station -= 1
        

def remove_city_research_station(bord_state, cities, research_station_cuonter=0):
    research_station_name = bord_state.research_stations.pop(research_station_cuonter)
    cities[research_station_name].research_station = False
    bord_state.num_research_station += 1


def remove_player_card(corent_player):
    for i, card in enumerate(corent_player.hand):
        if card == corent_player.corent_city:
            corent_player.hand.pop(i)

