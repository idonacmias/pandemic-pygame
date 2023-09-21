import pygame
from dataclasses import dataclass, field
from .cities import cities
from .constances import FIRST_CITY, MAX_RESEARCH_STATION, MAX_DISEASE_CUBE, INFACTION_SCALE_CUNTER, TOTAL_NUMBER_OF_EPIDEMIC_CARDS
from random import shuffle, randrange
from display import Color


@dataclass(init=True)
class BordState:

    def __init__(self):
        self.outbreack  = 0
        self.cure = {disease_color.name : 0 for disease_color in Color}

        self.disease_cube = [MAX_DISEASE_CUBE] * 4
        self.infaction_rate = 0
        self.infaction_scale_cunter = INFACTION_SCALE_CUNTER

        self.num_research_station = MAX_RESEARCH_STATION - 1
        self.research_stations = [FIRST_CITY]
        self.player_discard_cards = []
        self.infaction_discard_cards  = []
        self.player_cards = BordState.create_player_cards()
        self.infaction_cards = [city for city in cities.values()]
        
        shuffle(self.infaction_cards)

    @staticmethod
    def create_player_cards():
        city_cards = [city for city in cities.values()]
        events_cards = []
        player_cards = city_cards + events_cards
        shuffle(player_cards)
        player_cards_len = len(player_cards)
        stack_len = player_cards_len // TOTAL_NUMBER_OF_EPIDEMIC_CARDS
        for i in range(TOTAL_NUMBER_OF_EPIDEMIC_CARDS):
            i += 1
            epidemic_location = randrange(player_cards_len - stack_len * i,player_cards_len)
            print(f'epidemic_location: {epidemic_location}')
            player_cards.insert(epidemic_location, "epidemic")
        return player_cards