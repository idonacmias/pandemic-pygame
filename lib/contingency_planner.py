def contingency_planner_take_event_card(corent_player, picked_cards, bord_state):
    corent_player.contingency_planner_event_card = picked_cards[0]    
    corent_player.actions -= 1
    for i, card in enumerate(bord_state.player_discard_cards):
        if card == picked_cards[0]:
            bord_state.player_discard_cards.pop(i)

