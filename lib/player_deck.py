from .infaction import add_diseasse_to_city
from random import shuffle


def draw_from_deck(bord_state, corent_player, EpidemicCard, cities):
    '''Epidemic Card is a class, cannot be imported due to circular import  '''
    for _ in range(2):
        card = bord_state.players_deck[0]
        if type(card) ==  EpidemicCard:
            bord_state.player_discard_cards.append(card)
            epidemic_effect(bord_state, cities)

        else:
            corent_player.hand.append(card)

        bord_state.players_deck.pop(0)


def epidemic_effect(bord_state, cities):
    incrise_infaction(bord_state)
    infect_city(bord_state, cities)
    intensify(bord_state)
        

def incrise_infaction(bord_state):
    bord_state.infaction_rate += 1


def infect_city(bord_state, cities):
    card = bord_state.infaction_cards.pop(-1)
    city = cities[card.name]
    bord_state.infaction_discard_cards.append(card)
    outbreack_cities = []
    diseasse_color = card.color
    add_diseasse_to_city(city, diseasse_color, bord_state, cities, 3, outbreack_cities)
    

def intensify(bord_state):
    shuffle(bord_state.infaction_discard_cards)
    bord_state.infaction_cards = bord_state.infaction_discard_cards + bord_state.infaction_cards
    bord_state.infaction_discard_cards = []
 