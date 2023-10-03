from data import NUMBER_CARDS_NEEDED_TO_CURE

def discover_cure(bord_state, picked_cards, corent_player):
    if is_valid_cure(bord_state, picked_cards, corent_player):
        bord_state.cure[picked_cards[0].color.name] = 1
        corent_player.actions -= 1
        remove_cure_cards_from_palyer_haned(picked_cards, corent_player)
        picked_cards = []

    return picked_cards


def is_valid_cure(bord_state, picked_cards, corent_player):
    '''the order of the validation mater -> anti empty list'''
    if (is_number_of_card_for_cure_valid(picked_cards) and 
        is_cure_not_discoverd(picked_cards, bord_state) and
        is_player_in_reserch_station(corent_player) and 
        is_picked_cards_same_color(picked_cards, corent_player) and 
        is_picked_cards_in_player_hand(picked_cards, corent_player)):
        
        return True
    

def is_number_of_card_for_cure_valid(picked_cards):
    number_cards_needed_to_cure = NUMBER_CARDS_NEEDED_TO_CURE
    if len(picked_cards) == number_cards_needed_to_cure:
        return True


def is_cure_not_discoverd(picked_cards, bord_state):
    first_card = picked_cards[0]
    if bord_state.cure[first_card.color.name] == 0:
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
    for card in picked_cards[1:]:
        if card not in corent_player.hand:
            return False

    return True


def remove_cure_cards_from_palyer_haned(picked_cards, corent_player):
    for i, card in enumerate(corent_player.hand):
        if card in picked_cards:
            corent_player.hand.pop(i)


