import pygame
from .color import colors_palet
from .constances import INFACTION_SCALE_CUNTER, INFACTION_SCALE_POSITIONS, CURE_BAR_POINT, OUTBREAK_BAR_POINTS
from .Color import Color

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
        text_number = str(cunter[i])
    else:
        text_number = str(i)

    text_render = font.render(text_number, True, colors_palet[font_color])
    text_point = (point[0] - 5, point[1] - 7)    
    screen.blit(text_render, text_point)

def draw_medicen_bar(screen, cure=[0,2,1,2]):
    colors = list(Color.__members__)
    for color, point in enumerate(CURE_BAR_POINT):
        a,b,c,d = point[0], point[1], point[1] + 70, point[0] + 70
        squer_point = [(a, b), (a, c), (d, c), (d, b)]
        pygame.draw.polygon(surface=screen, color=colors_palet[colors[color]], points=squer_point)
        if cure[color] == 1:
            draw_medicen_symbol(screen, point)

        if cure[color] == 2:
            point = (point[0] + 35, point[1] + 35)
            draw_extinct_symbol(screen, point, colors[color])

def draw_medicen_symbol(screen, point):
    a,b,c,d = point[0] + 28, point[1] + 20, point[1] + 35, point[0] + 42
    squer_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['WHITE'], points=squer_point)
    
    circle_point = (point[0] + 35, point[1] + 50)
    pygame.draw.circle(surface=screen, color=colors_palet['WHITE'], center=circle_point, radius=15)

def draw_extinct_symbol(screen, point, backruond_color):
    pygame.draw.circle(surface=screen, color=colors_palet['WHITE'], center=point, radius=20)
    pygame.draw.circle(surface=screen, color=colors_palet[backruond_color], center=point, radius=15)
    a,b = (point[0] - 10, point[1] - 10), (point[0] + 10, point[1] + 10)
    pygame.draw.line(screen, colors_palet['WHITE'], a, b, 5)
    
