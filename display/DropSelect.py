import pygame
from .color import colors_palette



class DropSelect(object):

    WIDTH = 400
    HEIGHT = 50
    BACKRAOND_COLOR = 'BLUE'
    TEXT_COLOR = 'PINK'

    """docstring for DropSelect"""
    def __init__(self, options_list :  list , x :float, y :float):
        self.x = x
        self.y = y
        self.options = self.creat_options(options_list, x, y)
        self.colapse = True
        self.chosen_option = options_list[0]
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)

    def creat_options(self, options_list, x, y) -> 'list of DropSelectOption' :
        options = []
        for i, option in  enumerate(options_list):
            options.append(DropSelectOption(x, self.culculate__new_y(i, y), self.WIDTH, self.HEIGHT, option))

        return options


    def culculate__new_y(self, i :int, y :float) -> 'float':
        return y + (self.HEIGHT * i)


    def draw(self, screen, font) -> None:
        if self.colapse:
            pygame.draw.rect(screen, self.BACKRAOND_COLOR, self.rect)
            text_surface = font.render(self.chosen_option, True, self.TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

        else:
            for option in self.options:
                option.draw(screen, font)

    def handel_event(self, event):
        if not self.colapse:
            for option in self.options:
                new_option = option.handel_event(event)
                if new_option:
                    self.chosen_option = new_option
                    self.colapse = True
                    return

        elif event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.colapse = False


        
class DropSelectOption(pygame.Rect):
    """one option of DropSelect"""
    
    BACKRAOND_COLOR = 'BLUE'
    TEXT_COLOR = 'PINK'

    def __init__(self, x :float , y :float, width :float, height :float, option :str, ):
        super().__init__(x, y, width, height)
        self.option = option
        self.backraond_color = colors_palette[self.BACKRAOND_COLOR] 

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.BACKRAOND_COLOR, self)
        text_surface = font.render(self.option, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)


    def handel_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.collidepoint(event.pos):
            return self.option
