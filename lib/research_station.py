def builed_research_station(bord_state, corent_player, cities, government_grant, city_card=None, builed_city=None):
    if government_grant:
        if builed_city and not builed_city.research_station:
            add_city_research_station(bord_state, builed_city, cities)
            
        else:
            chose_city()

    elif (not corent_player.corent_city.research_station and 
          city_card and
          is_city_card_in_corent_player_hand(city_card, corent_player) and
          corent_player.role == 'Operations_Expert' and 
          corent_player.once_per_turn and
          city_card.name != corent_player.corent_city.name):

        corent_player.once_per_turn = False
        discard_card(city_card, corent_player)
        reduse_action(corent_player)
        add_city_research_station(bord_state, corent_player.corent_city, cities)

    elif (not corent_player.corent_city.research_station and
          corent_city_in_player_hand(corent_player)):
        
        remove_corent_city_player_card(corent_player)
        reduse_action(corent_player)
        add_city_research_station(bord_state, corent_player.corent_city, cities)


def is_city_card_in_corent_player_hand(city_card, corent_player):
    for card in corent_player.hand:
        if card == city_card:
            return True


def discard_card(city_card, corent_player):
    for i, card in enumerate(corent_player.hand):
        if card == city_card:
            corent_player.hand.pop(i)    


def corent_city_in_player_hand(corent_player):
    for card in corent_player.hand:
        if card.name == corent_player.corent_city.name:
            return True


def add_city_research_station(bord_state, builed_city, cities):
    if bord_state.num_research_station <= 0: remove_city_research_station(bord_state, cities) 
    builed_city.research_station = True
    bord_state.research_stations.append(builed_city.name)
    bord_state.num_research_station -= 1
        

def remove_city_research_station(bord_state, cities, research_station_cuonter=0):
    research_station_name = bord_state.research_stations.pop(research_station_cuonter)
    cities[research_station_name].research_station = False
    bord_state.num_research_station += 1


def reduse_action(corent_player):
    corent_player.actions -= 1


def remove_corent_city_player_card(corent_player):
    for i, card in enumerate(corent_player.hand):
        if card.name == corent_player.corent_city.name:
            card = corent_player.hand.pop(i)
            return card

