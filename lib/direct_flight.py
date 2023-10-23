def direct_flight(bord_state, corent_player, picked_cards, cities, picked_player):
    unlimited_movement = False
    if (len(picked_cards) == 1 and
        picked_cards[0] in corent_player.hand):

        chosen_card = picked_cards[0]
        if corent_player.role == 'Dispatcher' and picked_player:
            moved_player = picked_player 

        else:
            moved_player = corent_player 
            
        if moved_player.corent_city.name != chosen_card.name:
            moved_player.corent_city = cities[chosen_card.name]
        
        else: 
            unlimited_movement = True

        discard_card(corent_player, chosen_card, bord_state)
        if not unlimited_movement: corent_player.actions -= 1
        return unlimited_movement

def discard_card(corent_player, chosen_card, bord_state):
    for i, card in enumerate(corent_player.hand):
        if card == chosen_card: 
            corent_player.hand.pop(i)
            bord_state.player_discard_cards.append(card)
