import pygame
from dataclasses import dataclass, field
from display import Color

@dataclass
class City:
    name : str
    color : str
    population : int 
    routes : list
    point : tuple 
    diseasse_cubes : dict = field(default_factory=lambda: {disease_color.name : 0 for disease_color in Color})
    research_station = False

    def __post_init__(self):
        self.color = Color[self.color]

    def __str__(self):
        return f'{self.name} , {self.color} \n {self.diseasse_cubes}'
