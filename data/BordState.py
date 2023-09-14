import pygame
from dataclasses import dataclass, field




@dataclass
class BordState:
    outbreack  = 0
    cure  = [0] * 4
    disease_cube = [24] * 4
    infaction_rate = 0
    num_research_station = 5
    research_stations : list
