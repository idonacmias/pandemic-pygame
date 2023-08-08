import pygame

from color import colors_palet


from dataclasses import dataclass, field

from Color import Color
from constances import MAX_CUBE_IN_CITY, CITY_RADIUS

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

    # def infect(self, disease_pool, color):
    #     if self.disease_cubes[color - 1] < MAX_CUBE_IN_CITY:
    #         self.disease_cubes[color - 1] += 1
    #         disease_pool[color - 1] -= 1

    #     else:
    #         self.outbreack(disease_pool)
        
    #     print(self)

    # def outbreack(self, disease_pool):
    #     self.outbreack_bool = True
    #     print(f'{self.name} is outbreacking')
    #     for city in self.routes:
    #         if not city.outbreack_bool: 
    #             city.infect(disease_pool, self.color)

    # def epidemic_infect(self, disease_pool):
    #     city_disease = self.disease_cubes[self.color.value - 1]
    #     if city_disease + 3 > MAX_CUBE_IN_CITY:
    #         print('epidemic_infect!!!!!!!!!!!!')
    #         self.outbreack(disease_pool)

    #     disease_pool[self.color.value - 1] -= MAX_CUBE_IN_CITY - city_disease
    #     city_disease = 3







    #TODO: display in difrant class

    def click_lenth_from_center(self, muose_point):
        return abs(self.point[0] - muose_point[0]) + abs(self.point[1] - muose_point[1])



    def draw(self, screen, color, font):
        pygame.draw.circle(surface=screen, color=color, center=self.point , radius=CITY_RADIUS)
        if self.resarch_station:
            pygame.draw.circle(surface=screen, color=colors_palet['WHITE'], center=self.point , radius=10)


        text_surface = font.render(self.name, True, colors_palet['GREEN']) 
        screen.blit(text_surface, self.point)
