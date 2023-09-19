import pygame
from dataclasses import dataclass, field
from .cities import cities
from .constances import FIRST_CITY, MAX_RESEARCH_STATION, MAX_DISEASE_CUBE, INFACTION_SCALE_CUNTER
from random import shuffle


@dataclass
class BordState:
    outbreack  = 0
    cure  = [0] * 4
    disease_cube = [MAX_DISEASE_CUBE] * 4
    infaction_rate = 0
    infaction_scale_cunter = INFACTION_SCALE_CUNTER

    num_research_station = MAX_RESEARCH_STATION - 1
    research_stations = [FIRST_CITY]
    player_discard_cards = []
    infaction_discard_cards  = []
    player_cards = [city for city in cities.values()]
    infaction_cards = [city for city in cities.values()]
    
    shuffle(player_cards)
    shuffle(infaction_cards)
