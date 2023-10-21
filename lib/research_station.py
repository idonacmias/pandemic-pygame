def builed_research_station(bord_state, corent_player, cities, government_grant, city=None):
    if not government_grant:
        if is_player_have_city_card(corent_player):
            city = corent_player.corent_city         
            corent_player.actions -= 1
            card = remove_player_card(corent_player)
            card.picked = False
            bord_state.player_discard_cards.append(card)

    if city and not city.research_station:
        add_city_research_station(bord_state, city, cities)


def is_player_have_city_card(corent_player):
    for card in corent_player.hand:
        if card.name == corent_player.corent_city.name:
            return True


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
        if card.name == corent_player.corent_city.name:
            card = corent_player.hand.pop(i)
            return card
