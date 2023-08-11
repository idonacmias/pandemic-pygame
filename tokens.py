import pygame
from color import colors_palet
from card import draw_biohazerd
from constances import INFACTION_SCALE, CURE_POINT
from Color import Color

def draw_infaction_scale(screen, font, infaction_rate=0):
    TEXT = 0
    POINT = 1
    for i, data in enumerate(INFACTION_SCALE):
        if i == infaction_rate:
            pygame.draw.circle(surface=screen, color=colors_palet['SICK_GREEN'], center=data[POINT] , radius=20)

            text_render = font.render(str(data[TEXT]), True, colors_palet['YELLOW'])
            screen.blit(text_render, data[POINT])


        else:
            pygame.draw.circle(surface=screen, color=colors_palet['GREEN'], center=data[POINT] , radius=20)
    
            text_render = font.render(str(data[TEXT]), True, colors_palet['BLACK'])
            screen.blit(text_render, data[POINT])

def draw_medicen_bar(screen, cure=[0,0,0,0]):
    colors = list(Color.__members__)
    for color, point in enumerate(CURE_POINT):
        a,b,c,d = point[0], point[1], point[1] + 70, point[0] + 70
        squer_point = [(a, b), (a, c), (d, c), (d, b)]
        pygame.draw.polygon(surface=screen, color=colors_palet[colors[color]], points=squer_point)
