import pygame
from display import Color, CITY_RADIUS
from events import all_events


class City:
    
    def __init__(self, name, point, color, population, routes):
        self.name = name 
        self.color = Color[color] 
        self.population = population  
        self.routes = routes 
        self.point = point  
        self.diseasse_cubes = {disease_color.name : 0 for disease_color in Color}
        self.research_station = False
        self.radius = CITY_RADIUS
        self.rect = None

    def __str__(self):
        return f'{self.name} , {self.color} \n {self.diseasse_cubes}'


    def handle_event(self, event, chosen_city):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            pygame.event.post(pygame.event.Event(all_events['CLICK_ON_CITY']))
            chosen_city = self
        
        return chosen_city



