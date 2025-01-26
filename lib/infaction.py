def first_infaction(bord_state, cities):
    for num_diseasse_cubes in range(1, 4):
        infected_cards_drawn = draw_infected_cards(bord_state, 3)
        for card in infected_cards_drawn:
            city = cities[card.name]
            diseasse_color = city.color.name
            add_diseasse_to_city(city, diseasse_color, bord_state, cities, players=None, num_diseasse_cubes=num_diseasse_cubes)

def draw_infected_cards(bord_state, num_card_to_draw=None):
    if not num_card_to_draw: num_card_to_draw = bord_state.infaction_scale_cunter[bord_state.infaction_rate]

    infected_cards_drawn = bord_state.infaction_cards[:num_card_to_draw]
    bord_state.infaction_cards = bord_state.infaction_cards[num_card_to_draw:]
    bord_state.infaction_discard_cards += infected_cards_drawn
    return infected_cards_drawn


def infected_phase(bord_state, cities, quarantined_cities, players):
    infected_cards_drawn = draw_infected_cards(bord_state)
    for card in infected_cards_drawn:
        city = cities[card.name]
        diseasse_color = city.color.name
        
        add_diseasse_to_city(city, diseasse_color, bord_state, cities, players, quarantined_cities=quarantined_cities, outbreack_cities=[])



def add_diseasse_to_city(city, diseasse_color, bord_state, cities, players, quarantined_cities=[], num_diseasse_cubes=1, outbreack_cities=None ):
    '''dont forget to update infect_city in player_deck'''
    if is_city_allow_to_be_infected(bord_state, quarantined_cities, players, city, diseasse_color):
        if city.diseasse_cubes[diseasse_color] < 3:
            city.diseasse_cubes[diseasse_color] += num_diseasse_cubes

        elif city not in outbreack_cities:
            outbreack(city, cities, outbreack_cities, diseasse_color, bord_state, quarantined_cities, players)


def is_city_allow_to_be_infected(bord_state, quarantined_cities, players, city, diseasse_color):
    if not (bord_state.cure[diseasse_color] == 2 or 
           city.name in quarantined_cities or 
           is_medic_prevent_diseasse_sprading(players, bord_state, diseasse_color, city)):

        return True


def is_medic_prevent_diseasse_sprading(players, bord_state, diseasse_color, city): 
    if bord_state.cure[diseasse_color] == 1 and players:
        for player in players:
            if (player.role == 'Medic' and
                player.corent_city == city):
                return True


def outbreack(city, cities, outbreack_cities, diseasse_color, bord_state, quarantined_cities, players):
    outbreack_cities.append(city)
    bord_state.outbreack += 1
    for city_name in city.routes:
        city = cities[city_name]
        add_diseasse_to_city(city, diseasse_color, bord_state, players=players, quarantined_cities=quarantined_cities, outbreack_cities=outbreack_cities, cities=cities)

