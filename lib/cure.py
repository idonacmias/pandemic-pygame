from data import NUMBER_CARDS_NEEDED_TO_CURE

def discover_cure(bord_state, picked_cards, corent_player):
    if is_valid_cure(bord_state, picked_cards, corent_player):
        bord_state.cure[picked_cards[0].color.name] = 1
        corent_player.actions -= 1
        picked_cards = []

    return picked_cards

def is_valid_cure(bord_state, picked_cards, corent_player):
    first_card = picked_cards[0]
    if bord_state.cure[first_card.color.name] != 0:
        return False

    number_cards_needed_to_cure = NUMBER_CARDS_NEEDED_TO_CURE
    if len(picked_cards) != number_cards_needed_to_cure:
        return False

    for card in picked_cards[1:]:
        if card.color != first_card.color or card not in corent_player.hand:
            break

    else:
        return True

