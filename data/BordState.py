import pygame
from dataclasses import dataclass, field




@dataclass
class BordState:
    outbreack  = 0
    cure  = [0] * 4
    cure_cube = [24] * 4
    