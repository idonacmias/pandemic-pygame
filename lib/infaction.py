def first_infaction(bord_state, cities):
    for num_diseasse_cubes in range(1, 4):
        infected_cards_drawn = draw_infected_cards(bord_state, 3)
        for card in infected_cards_drawn:
            city = cities[card.name]
            diseasse_color = city.color.name
            add_diseasse_to_city(city, diseasse_color, bord_state, cities, num_diseasse_cubes=num_diseasse_cubes)

def draw_infected_cards(bord_state, num_card_to_draw=None):
    if not num_card_to_draw: num_card_to_draw = bord_state.infaction_scale_cunter[bord_state.infaction_rate]

    infected_cards_drawn = bord_state.infaction_cards[:num_card_to_draw]
    bord_state.infaction_cards = bord_state.infaction_cards[num_card_to_draw:]
    bord_state.infaction_discard_cards += infected_cards_drawn
    return infected_cards_drawn


def infected_phase(bord_state, cities):
    infected_cards_drawn = draw_infected_cards(bord_state)
    for card in infected_cards_drawn:
        city = cities[card.name]
        diseasse_color = city.color.name
        
        add_diseasse_to_city(city, diseasse_color, cities=cities, bord_state=bord_state, outbreack_cities=[])



def add_diseasse_to_city(city, diseasse_color, bord_state, cities, num_diseasse_cubes=1, outbreack_cities=None ):
    '''dont forget to update infect_city in player_deck'''
    if bord_state.cure[diseasse_color] == 2: return 
    if city.diseasse_cubes[diseasse_color] < 3:
        city.diseasse_cubes[diseasse_color] += num_diseasse_cubes

    elif city not in outbreack_cities:
        outbreack(city, cities, outbreack_cities, diseasse_color, bord_state)


def outbreack(city, cities, outbreack_cities, diseasse_color, bord_state):
    outbreack_cities.append(city)
    bord_state.outbreack += 1
    for city_name in city.routes:
        city = cities[city_name]
        add_diseasse_to_city(city, diseasse_color, bord_state, outbreack_cities=outbreack_cities, cities=cities)

