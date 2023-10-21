import pygame
from display import colors_palet
from events import CLICK_ON_CARD

class Card(pygame.Rect):
    
    """abstract of a Card: DO NOT USE!!!!"""

    def __init__(self, x, y, width=180, height=200):
        super().__init__(x, y, width, height)
        self.color = 'GRAY' 
        self.text_color = 'GRAY'
        self.backruond_color = self.color

    def draw(self, screen, font):
        pygame.draw.rect(screen, colors_palet[self.backruond_color], self)
        for i, text in enumerate(self.texts):
            point = (self.midtop[0], self.midtop[1] + (i + 1) * 40)
            self.draw_text(screen, font, point, text)     


    def draw_text(self, screen, font, point, text):     
        text_surface = font.render(text, True, colors_palet[self.text_color])
        text_rect = text_surface.get_rect(center=point)
        screen.blit(text_surface, text_rect)


    def handle_event(self, event, chosen_card):
        if event.type == pygame.MOUSEMOTION and self.collidepoint(event.pos):
            self.backruond_color = 'PINK'

        elif event.type == pygame.MOUSEMOTION:
            self.backruond_color = self.color     

        if event.type == pygame.MOUSEBUTTONDOWN and self.collidepoint(event.pos):
            pygame.event.post(pygame.event.Event(CLICK_ON_CARD))
            chosen_card = self
        
        return chosen_card


class EpidemicCard(Card):
    def __init__(self, x, y, width=180, height=200):
        super().__init__(x, y, width, height)
        self.color = 'SICK_GREEN'
        self.backruond_color = self.color
        self.text_color = 'BLACK'
        self.texts = ['Epidemic', 'incrise infaction', 'infect city', 'intensify']


class PlayerCard(Card):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.picked = False


    def __str__(self):
        return f'{self.name}, {self.color}'

    def __repr__(self):
        return self.__str__()

    def draw(self, screen, font):
        if self.picked:
            rect = pygame.Rect(0, 0, 200, 220)
            rect.center = self.center
            pygame.draw.rect(screen, colors_palet['WHITE'], rect)

        super().draw(screen, font)        


class CityCard(PlayerCard):
    
    def __init__(self, city, x, y, width=180, height=200):
        super().__init__(x, y, width, height)
        self.color = city.color.name 
        self.backruond_color = self.color
        self.text_color = 'GRAY'
        self.name = city.name 
        self.population = city.population 
        self.texts = ['city name:', self.name, 'city population:', str(self.population)]


class EventCard(PlayerCard):

    def __init__(self, x, y, callback, name, description):
        super().__init__(x, y, width=180, height=200)
        self.color = 'YELLOW'
        self.backruond_color = self.color
        self.text_color = 'BLACK'
        self.name = name
        self.description = description
        self.callback = callback
        self.texts = ['Event:', self.name, 'description:', self.description]


    def use_event_card(self):
        pygame.event.post(pygame.event.Event(CLICK_ON_CARD))
        pygame.event.post(pygame.event.Event(self.callback))
        

class InfactionCard(PlayerCard):
    def __init__(self, city, x, y, width=180, height=200):
        super().__init__(x, y, width, height)
        self.color = city.color.name 
        self.backruond_color = self.color
        self.text_color = 'GRAY'
        self.name = city.name 
        self.population = city.population 
        self.texts = ['city name:', self.name, 'city population:', str(self.population)]

