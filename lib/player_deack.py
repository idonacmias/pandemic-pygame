from .infaction import add_diseasse_to_city
from random import shuffle



def draw_from_deack(bord_state, corent_player):
    for _ in range(2):
        card = bord_state.players_deck[0]
        if card == 'epidemic':
            bord_state.player_discard_cards.append('epidemic')
            epidemic_effect(bord_state)

        else:
            corent_player.hand.append(card)

        bord_state.players_deck.pop(0)


def epidemic_effect(bord_state):
    incrise_infaction(bord_state)
    infect_city(bord_state)
    intensify(bord_state)
        


def incrise_infaction(bord_state):
    bord_state.infaction_rate += 1


def infect_city(bord_state):
    city = bord_state.infaction_cards.pop(-1)
    bord_state.infaction_discard_cards.append(city)
    outbreack_cities = []
    diseasse_color = city.color
    add_diseasse_to_city(city, diseasse_color, bord_state, 3, outbreack_cities)
    

def intensify(bord_state):
    shuffle(bord_state.infaction_discard_cards)
    bord_state.infaction_cards = bord_state.infaction_discard_cards + bord_state.infaction_cards
    bord_state.infaction_discard_cards = []
 