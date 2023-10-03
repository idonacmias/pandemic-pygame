def direct_flight(corent_player, picked_cards):
    print('direct_flight')
    if (len(picked_cards) == 1 and
        picked_cards[0] in corent_player.hand):

        city = picked_cards[0]
        if (corent_player.corent_city != city):
            remove_city_from_hand(corent_player, city)
            corent_player.corent_city = city
            corent_player.actions -= 1

def remove_city_from_hand(corent_player, city):
    for i, card in enumerate(corent_player.hand):
        if card == city: 
            corent_player.hand.pop(i)