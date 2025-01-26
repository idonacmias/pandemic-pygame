from data import NUMBER_CARDS_NEEDED_TO_CURE
from .diseasse import try_eradication


def discover_cure(bord_state, picked_cards, corent_player, cities):
    if is_valid_cure(bord_state, picked_cards, corent_player):
        color_name = picked_cards[0].color
        bord_state.cure[color_name] = 1
        remove_cure_cards_from_palyer_haned(picked_cards, corent_player)
        bord_state.player_discard_cards += picked_cards
        corent_player.use_action()
        try_eradication(cities, color_name, bord_state)
                

def is_valid_cure(bord_state, picked_cards, corent_player):
    '''the order of the validation mater -> anti empty list'''
    if (is_number_of_card_for_cure_valid(picked_cards, corent_player) and 
        is_cure_not_discoverd(picked_cards, bord_state) and
        is_player_in_reserch_station(corent_player) and 
        is_picked_cards_same_color(picked_cards, corent_player) and 
        is_picked_cards_in_player_hand(picked_cards, corent_player)):
        
        return True
    

def is_number_of_card_for_cure_valid(picked_cards, corent_player):
    number_cards_needed_to_cure = NUMBER_CARDS_NEEDED_TO_CURE
    if corent_player.role == 'Scientist': number_cards_needed_to_cure -= 1
    if len(picked_cards) == number_cards_needed_to_cure:
        return True

    print('not enugh cards')

def is_cure_not_discoverd(picked_cards, bord_state):
    first_card = picked_cards[0]
    if bord_state.cure[first_card.color] == 0:
        return True


def is_player_in_reserch_station(corent_player):
    if corent_player.corent_city.research_station:
        return True


def is_picked_cards_same_color(picked_cards, corent_player):
    first_card = picked_cards[0]
    for card in picked_cards[1:]:
        if card.color != first_card.color:
            return False

    return True


def is_picked_cards_in_player_hand(picked_cards, corent_player):
    for card in picked_cards:
        if card not in corent_player.hand:
            return False

    return True


def remove_cure_cards_from_palyer_haned(picked_cards, corent_player):
    corent_player.hand = [card for card in corent_player.hand if card not in picked_cards]

