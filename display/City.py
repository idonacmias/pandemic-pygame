import pygame
from dataclasses import dataclass, field

from .color import colors_palet
from .Color import Color
from .constances import CITY_RADIUS, EDGE_CITIES

@dataclass
class City:
    name : str
    color : str
    population : int 
    routes : list
    point : tuple 
    disease_cubes : list = field(default_factory=lambda: [0]*4)
    resarch_station = False
    outbreack_bool = False

    def __post_init__(self):
        self.color = Color[self.color]

    def __str__(self):
        return f'{self.name} , {self.color} \n {self.disease_cubes}'
