import pygame 
from .color import colors_palette


class Botton(pygame.Rect):

    def __init__(self, x, y, width, height, text, callback):
        super().__init__(x, y, width, height)
        self.text = text
        self.callback = callback
        self.color = colors_palette['GRAY']        


    def __str__(self):
        return self.text


    def __repr__(self):
        return f'Botton: {self.__str__()}'


    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)

    def handel_event(self, event):
        if event.type == pygame.MOUSEMOTION and self.collidepoint(event.pos):
            self.color = colors_palette['PINK']

        elif event.type == pygame.MOUSEMOTION:
            self.color = colors_palette['GRAY']      

        if event.type == pygame.MOUSEBUTTONDOWN and self.collidepoint(event.pos):
            pygame.event.post(pygame.event.Event(self.callback))




                