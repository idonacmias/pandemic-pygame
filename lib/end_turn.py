from .player_deck import draw_from_deck
from .infaction import infected_phase
from data import ACTION_PER_TURN


def end_turn(bord_state, corent_player, cities, players, one_quiet_night, cycle_player):
    quarantined_cities = []
    for player in players:
        if player.role == 'Quarantine_Specialist':
            quarantined_cities += player.corent_city.routes + [player.corent_city.name]
        
    quarantined_cities = set(quarantined_cities)
    draw_from_deck(bord_state, corent_player, cities, quarantined_cities)
    if not one_quiet_night: infected_phase(bord_state, cities, quarantined_cities)
    corent_player = next(cycle_player)
    corent_player.once_per_turn = True
    corent_player.actions = ACTION_PER_TURN
    return corent_player 
