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


def witch_click_on(mouse_point):
    BUTTONS_DATA = zip(BUTTONS_POINTS, BUTTONS_TEXTS)
    for button_point, text in BUTTONS_DATA:
        square_points = [button_point, (button_point[0] + BUTTON_WHIDTH, button_point[1] + BUTTON_HIGHT)]
        if is_in_squer(square_points, mouse_point):
            print(text)
            return text                 

def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]