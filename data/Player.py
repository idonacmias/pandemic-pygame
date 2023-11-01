from .constances import ACTION_PER_TURN
from random import choice
import pygame
from events import all_events


class Player():

    players_roles = {'Quarantine_Specialist' : 'DARK_GREEN', #V  #no desisses cube in the neer by cities
                     'Dispatcher' : 'PURPLE',            #V  #can move other player in his turn
                     'Operations_Expert' : 'GREEN',     #V  #can builed reserch station without card, can move anywere form reserch station by discarding card 
                     'Medic' : 'ORENGE',                 #V  #treat all diseasse cube in city of the same color, treat diseasse with no action if cure is discoverd 
                     'Researcher' : 'BRAUN',            #V  #can give his card, even if city shared is not the card thet move
                     'Scientist' : 'WHITE',             #V  #can discover cure with 4 card insted of 5
                     'Contingency_Planner' : 'TEAL'}   #as an action can store on discard event card from discard player cards, and use it as evet

    def __init__(self, Player_cards, starter_city, role=False):
        if role:
            self.role = role
            self.color = self.players_roles[role]

        else:
            self.role, self.color = choice(list(self.players_roles.items()))

        self.corent_city = starter_city
        self.actions = ACTION_PER_TURN
        self.hand = Player_cards
        self.once_per_turn = True
        self.contingency_planner_event_card = None



    def use_action(self):
        self.actions -= 1
        if self.actions == 0:
            pygame.event.post(pygame.event.Event(all_events['END_TURN']))
