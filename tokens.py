import pygame
from color import colors_palet
from card import draw_biohazerd
from constances import INFACTION_SCALE_CUNTER, INFACTION_SCALE_POSITIONS, CURE_BAR_POINT, OUTBREAK_BAR_POINTS
from Color import Color

def draw_infaction_scale(screen, font, rate=0):
    draw_bar(screen, font, INFACTION_SCALE_POSITIONS, INFACTION_SCALE_CUNTER, rate=rate)

def draw_outbreak_bar(screen, font, rate=0):
    draw_bar(screen, font, OUTBREAK_BAR_POINTS, rate=rate)

def draw_bar(screen, font, points, cunter=None, rate=0):
    for i, point in enumerate(points):
        if i == rate:
            draw_bar_circle(screen, font, i, 'SICK_GREEN', 'YELLOW', point, cunter)

        else:
            draw_bar_circle(screen, font, i, 'GREEN', 'BLACK', point, cunter)

def draw_bar_circle(screen, font, i, circle_color, font_color, point, cunter):
    pygame.draw.circle(surface=screen, color=colors_palet[circle_color], center=point , radius=20)
    if cunter:
        text_render = font.render(str(cunter[i]), True, colors_palet[font_color])

    else:
        text_render = font.render(str(i + 1), True, colors_palet[font_color])

    screen.blit(text_render, point)

def draw_medicen_bar(screen, cure=[0,0,0,0]):
    colors = list(Color.__members__)
    for color, point in enumerate(CURE_BAR_POINT):
        a,b,c,d = point[0], point[1], point[1] + 70, point[0] + 70
        squer_point = [(a, b), (a, c), (d, c), (d, b)]
        pygame.draw.polygon(surface=screen, color=colors_palet[colors[color]], points=squer_point)


