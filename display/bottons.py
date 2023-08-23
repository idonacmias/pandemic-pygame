import pygame

from .constances import BUTTONS_POINTS,BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT
from .color import colors_palet


def draw(screen, font):
    BUTTONS_DATA = zip(BUTTONS_POINTS, BUTTONS_TEXTS)
    for point, text in BUTTONS_DATA:
        draw_squer(screen, point)
        text_render = font.render(text, True, colors_palet['BLACK'])
        text_point = (point[0] + 10, point[1])    
        screen.blit(text_render, text_point)

def draw_squer(screen, point):
    square_points = [point, (point[0] + BUTTON_WHIDTH, point[1]), (point[0] + BUTTON_WHIDTH, point[1] + BUTTON_HIGHT), (point[0], point[1] + BUTTON_HIGHT)]
    pygame.draw.polygon(surface=screen, color=colors_palet['GRAY'], points=square_points)

