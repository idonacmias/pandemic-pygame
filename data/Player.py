from .constances import ACTION_PER_TURN, players_roles
from random import choice
import pygame
from events import all_events


class Player():


    def __init__(self, Player_cards, starter_city, role):
        if role == 'random role':
            self.role, self.color = choice(list(players_roles.items()))

        else:
            self.role = role
            self.color = players_roles[role]

        self.corent_city = starter_city
        self.actions = ACTION_PER_TURN
        self.hand = Player_cards
        self.once_per_turn = True
        self.contingency_planner_event_card = None



    def use_action(self):
        self.actions -= 1
        if self.actions == 0:
            pygame.event.post(pygame.event.Event(all_events['END_TURN']))
