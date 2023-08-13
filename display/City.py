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

    def click_lenth_from_center(self, muose_point):
        return abs(self.point[0] - muose_point[0]) + abs(self.point[1] - muose_point[1])

    def draw(self, screen, color, font):
        pygame.draw.circle(surface=screen, color=color, center=self.point , radius=CITY_RADIUS)
        if self.resarch_station:
            pygame.draw.circle(surface=screen, color=colors_palet['WHITE'], center=self.point , radius=10)

        font_point = (self.point[0] - 5 * len(self.name), self.point[1] + 20)        
        text_surface = font.render(self.name, True, colors_palet['WHITE']) 
        screen.blit(text_surface, font_point)


    def conect_routes(self, screen, cities, font):
        for other_city_name in self.routes:
            other_city_point = cities[other_city_name].point
            if self.is_edge_conection(other_city_point):
                shadow_point = City.clculate_shadow_point(self.point, other_city_point)
                pygame.draw.line(screen, colors_palet['PINK'], self.point, shadow_point, 2)

                text_render = font.render(other_city_name, True, colors_palet['WHITE'])
                text_point_x = shadow_point[0] if shadow_point[0] < 500 else shadow_point[0] - 220    
                text_point = (text_point_x, shadow_point[1] - 50)
                screen.blit(text_render, text_point)

            else:
                other_city = cities[other_city_name]
                pygame.draw.line(screen, colors_palet['PINK'], self.point, other_city.point, 2)

    def is_edge_conection(self, other_city_point):
        return self.name in EDGE_CITIES and abs(other_city_point[0] - self.point[0]) > 500

    @staticmethod
    def clculate_shadow_point(point, other_point):
        if point[0] < 500:
            shadow_point = (0, other_point[1] // 2)

        else:
            shadow_point = (2000, point[1])

        return shadow_point