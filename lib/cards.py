def share_knowledge(corent_player, other_player, picked_cards):
    if (other_player != None and
        corent_player.corent_city == other_player.corent_city and
        corent_player != other_player and
        picked_cards):

        serched_card = picked_cards[-1]

        if serched_card in corent_player.hand and (serched_card == corent_player.corent_city):
            card_location = serch_card_in_list(corent_player.hand, serched_card)
            move_cards(corent_player, other_player, card_location)
            corent_player.actions -= 1

        elif serched_card in other_player.hand and (serched_card == corent_player.corent_city):
            card_location = serch_card_in_list(other_player.hand, serched_card)
            move_cards(other_player, corent_player, card_location)
            corent_player.actions -= 1


def serch_card_in_list(list_of_cards, serched_card):
    for card_location, card in enumerate(list_of_cards):
        if card == serched_card: 
            return card_location


def move_cards(give_player, take_player, card_locatin):
    card = give_player.hand.pop(card_locatin)
    take_player.hand.append(card)


