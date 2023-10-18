def direct_flight(bord_state, corent_player, picked_cards, cities):
    print('direct_flight')
    if (len(picked_cards) == 1 and
        picked_cards[0] in corent_player.hand):

        chosen_card = picked_cards[0]
        if (corent_player.corent_city.name != chosen_card.name):
            remove_city_from_hand(corent_player, chosen_card)
            bord_state.player_discard_cards += picked_cards
            corent_player.corent_city = cities[chosen_card.name]
            corent_player.actions -= 1

def remove_city_from_hand(corent_player, chosen_card):
    for i, card in enumerate(corent_player.hand):
        if card == chosen_card: 
            corent_player.hand.pop(i)