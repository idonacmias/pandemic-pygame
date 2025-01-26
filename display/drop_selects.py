from data import Player
from .DropSelect import DropSelect



def costum_game_drop_select(num_players=2):
    players_drop_select = [create_player_drop_select(i) for i in range(1, num_players + 1)]
    players_drop_select.reverse()
    return players_drop_select

def create_player_drop_select(player_index):
    Player_option = ['random role'] + list(Player.players_roles.keys())
    return DropSelect(Player_option, 1120, 170 + (player_index - 1) * 60)


def remove_player(players_drop_select):
    players_drop_select.pop(0)
    return players_drop_select


def add_player(players_drop_select):
    players_drop_select.insert(0, create_player_drop_select(len(players_drop_select) + 1))
    return players_drop_select


drop_selects = {'costum_game' : costum_game_drop_select(num_players=2)}


