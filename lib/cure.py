def discover_cure(bord_state, piked_cards, corent_player):
    if is_valid_cure(bord_state, piked_cards, corent_player):
        bord_state.cure[piked_cards[0].color.name] = 1
        corent_player.actions -= 1
        piked_cards = []

    return piked_cards

def is_valid_cure(bord_state, piked_cards, corent_player):
    first_card = piked_cards[0]
    if bord_state.cure[first_card.color.name] == 0:
        for card in piked_cards[1:]:
            if card.color != first_card.color or card not in corent_player.hand:
                break

        else:
            return True

