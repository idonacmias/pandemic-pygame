from .constances import ACTION_PER_TURN, FIRST_CITY


class Player():
    """docstring for Player"""
    def __init__(self, color, Player_cards):
        self.color = color
        self.corent_city_name = FIRST_CITY
        self.actions = ACTION_PER_TURN
        self.hand = Player_cards