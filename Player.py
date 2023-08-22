from constances import ACTION_PER_TURN


class Player():
    """docstring for Player"""
    def __init__(self, color, corent_city_name):
        self.color = color
        self.corent_city_name = corent_city_name
        self.actions = ACTION_PER_TURN