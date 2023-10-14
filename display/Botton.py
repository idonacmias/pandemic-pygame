import pygame

from .constances import BUTTON_WHIDTH, BUTTON_HIGHT
from .color import colors_palet


def draw(screen, font, points_text_zip):
    for point, text in points_text_zip:
        draw_squer(screen, point)
        text_render = font.render(text, True, colors_palet['BLACK'])
        text_point = (point[0] + 10, point[1])    
        screen.blit(text_render, text_point)


def draw_squer(screen, point):
    square_points = [point, (point[0] + BUTTON_WHIDTH, point[1]), (point[0] + BUTTON_WHIDTH, point[1] + BUTTON_HIGHT), (point[0], point[1] + BUTTON_HIGHT)]
    pygame.draw.polygon(surface=screen, color=colors_palet['GRAY'], points=square_points)

