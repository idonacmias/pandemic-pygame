import pygame
from .color import colors_palet
from .constances import INFACTION_SCALE_POSITIONS, CURE_BAR_POINT, OUTBREAK_BAR_POINTS, BAR_CIRCLE_RADIUS
from .Color import Color

def draw_infaction_rate(screen, font, bord_state):
    draw_bar(screen, font, INFACTION_SCALE_POSITIONS, bord_state.infaction_rate, bord_state.infaction_scale_cunter)

def draw_outbreak_bar(screen, font, rate):
    draw_bar(screen, font, OUTBREAK_BAR_POINTS, rate)

def draw_bar(screen, font, points, rate, cunter=None):
    for i, point in enumerate(points):
        if i == rate:
            circle_color = 'SICK_GREEN'
            font_color = 'YELLOW'

        else:
            circle_color = 'GREEN'
            font_color = 'BLACK'
        
        if cunter:
            text_number = str(cunter[i])

        else:
            text_number = str(i)



        draw_bar_circle(screen, font, text_number, circle_color, font_color, point)


def draw_bar_circle(screen, font, text_number, circle_color, font_color, point):
    pygame.draw.circle(surface=screen, color=colors_palet[circle_color], center=point , radius=BAR_CIRCLE_RADIUS)
    text_render = font.render(text_number, True, colors_palet[font_color])
    text_point = (point[0] - 5, point[1] - 7)    
    screen.blit(text_render, text_point)

def draw_medicen_bar(screen, cure):
    colors = list(Color.__members__)
    for color, point in enumerate(CURE_BAR_POINT):
        a,b,c,d = point[0], point[1], point[1] + 70, point[0] + 70
        squer_point = [(a, b), (a, c), (d, c), (d, b)]
        pygame.draw.polygon(surface=screen, color=colors_palet[colors[color]], points=squer_point)
        if cure[colors[color]] == 1:
            draw_medicen_symbol(screen, point)

        if cure[colors[color]] == 2:
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
    

