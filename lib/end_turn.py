from data import ACTION_PER_TURN


def next_player(cycle_player):
    corent_player = next(cycle_player)
    corent_player.once_per_turn = True
    corent_player.actions = ACTION_PER_TURN
    return corent_player 


def quarantine_specialist_effect(players):
    quarantined_cities = []
    for player in players:
        if player.role == 'Quarantine_Specialist':
            quarantined_cities += player.corent_city.routes + [player.corent_city.name]
        
    quarantined_cities = set(quarantined_cities)
    return quarantined_cities