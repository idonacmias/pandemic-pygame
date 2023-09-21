from data import cities



def first_infaction(bord_state):
    for num_diseasse_cubes in range(1, 4):
        infected_cards_drawn = draw_infected_cards(bord_state, 3)
        for city in infected_cards_drawn:
            diseasse_color = city.color
            add_diseas_to_city(city, diseasse_color, num_diseasse_cubes=num_diseasse_cubes)


def infected_phase(bord_state):
    infected_cards_drawn = draw_infected_cards(bord_state)
    for city in infected_cards_drawn:
        diseasse_color = city.color
        if bord_state.cure[diseasse_color.name] < 2:
            add_diseas_to_city(city, diseasse_color, outbreack_cities=[], bord_state=bord_state)


def draw_infected_cards(bord_state, num_card_to_draw=None):
    if not num_card_to_draw: num_card_to_draw = bord_state.infaction_scale_cunter[bord_state.infaction_rate]

    infected_cards_drawn = bord_state.infaction_cards[:num_card_to_draw]
    bord_state.infaction_cards = bord_state.infaction_cards[num_card_to_draw:]
    bord_state.infaction_discard_cards += infected_cards_drawn
    return infected_cards_drawn


def add_diseas_to_city(city, diseasse_color, num_diseasse_cubes=1, outbreack_cities=None, bord_state=None):
    if city.diseasse_cubes[diseasse_color] < 3:
        city.diseasse_cubes[diseasse_color] += num_diseasse_cubes

    elif city not in outbreack_cities:
        outbreack(city, outbreack_cities, diseasse_color, bord_state)


def outbreack(city, outbreack_cities, diseasse_color, bord_state):
    outbreack_cities.append(city)
    bord_state.outbreack += 1
    for city_name in city.routes:
        add_diseas_to_city(cities[city_name], diseasse_color, outbreack_cities=outbreack_cities, bord_state=bord_state)

