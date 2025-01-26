import pygame
from .color import colors_palette
import pygame

class Label(pygame.Rect):
    """docstring for label"""
    def __init__(self, x, y, width, height, text, backraond_color, text_color):
        super().__init__(x, y, width, height)
        self.text = text
        self.backraond_color = colors_palette[backraond_color]        
        self.text_color = colors_palette[text_color]

    def __str__(self):
        return self.text


    def __repr__(self):
        return f'Label: {self.__str__()}'


    def draw(self, screen, font):
        pygame.draw.rect(screen, self.backraond_color, self)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)

