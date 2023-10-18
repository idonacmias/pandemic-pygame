from .constances import ACTION_PER_TURN


class Player():
    def __init__(self, color, Player_cards, starter_city):
        self.color = color
        self.corent_city = starter_city
        self.actions = ACTION_PER_TURN
        self.hand = Player_cards