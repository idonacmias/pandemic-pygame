from .move_to_city import clear_discovered_cure_diseasse


def direct_flight(bord_state, corent_player, picked_cards, cities, picked_player):
    unlimited_movement = False
    if (len(picked_cards) == 1 and
        picked_cards[0] in corent_player.hand):

        chosen_card = picked_cards[0]
        moving_player = dispacher_choose_player_to_move(corent_player, picked_player)    
        if moving_player.corent_city.name == chosen_card.name:
            unlimited_movement = True
        
        elif operations_expert_movment(corent_player, chosen_card):
            unlimited_movement = True
            corent_player.once_per_turn = False

        else: 
            moving_player.corent_city = cities[chosen_card.name]
            if moving_player.role == 'Medic': 
                clear_discovered_cure_diseasse(bord_state, moving_player, cities)
        

        discard_card(corent_player, chosen_card, bord_state)
        if not unlimited_movement: corent_player.use_action()
        return unlimited_movement

def discard_card(corent_player, chosen_card, bord_state):
    for i, card in enumerate(corent_player.hand):
        if card == chosen_card: 
            corent_player.hand.pop(i)
            bord_state.player_discard_cards.append(card)



def dispacher_choose_player_to_move(corent_player, picked_player):
    if corent_player.role == 'Dispatcher' and picked_player:
        moving_player = picked_player 

    else:
        moving_player = corent_player 
    
    return  moving_player        


def operations_expert_movment(corent_player, chosen_card):
    if (corent_player.role == 'Operations_Expert' and 
        corent_player.once_per_turn and
        corent_player.corent_city.research_station):

        return True