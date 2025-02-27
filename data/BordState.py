import pygame
from dataclasses import dataclass, field
from random import shuffle, randrange
from .Card import CityCard, EpidemicCard, EventCard, InfactionCard
from .constances import FIRST_CITY, MAX_RESEARCH_STATION, MAX_DISEASE_CUBE, INFACTION_SCALE_CUNTER
from display import Color
from .event_card import EVENTS_CARDS_ZIP


@dataclass(init=True)
class BordState:

    def __init__(self, cities):
        self.outbreack  = 0
        self.cure = {disease_color.name : 0 for disease_color in Color}
        self.disease_cube = [MAX_DISEASE_CUBE] * 4
        self.infaction_rate = 0
        self.infaction_scale_cunter = INFACTION_SCALE_CUNTER

        self.num_research_station = MAX_RESEARCH_STATION - 1
        self.research_stations = [FIRST_CITY]
        self.player_discard_cards = []
        self.infaction_discard_cards  = []
        self.players_deck = BordState.create_player_cards(cities)
        self.infaction_cards = [InfactionCard(city, 200, 200) for city in cities.values()]
        shuffle(self.infaction_cards)


    @staticmethod
    def create_player_cards(cities):
        city_cards = [CityCard(city, 200, 200) for city in cities.values()]
        events_cards = [EventCard(200, 200, callback, name, description) for callback, name, description in EVENTS_CARDS_ZIP]
        players_deck = events_cards + city_cards
        shuffle(players_deck)
        return players_deck


    def insert_epidemic(self, num_of_epidemic):
        split_deack = len(self.players_deck) // num_of_epidemic
        for i in range(num_of_epidemic):
            position = randrange(split_deack) + (i * split_deack)
            self.players_deck.insert(position, EpidemicCard(200,200))

