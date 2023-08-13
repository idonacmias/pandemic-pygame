import pygame
import math

from .constances import CARD_HALF_WHIDTH, CARD_HALF_HIGHT, INFACTION_CARDS_POSITION, DISCARD_INFACTION_CARDS_POSITION, DISCARD_PLAYERS_CARDS_POSITION, PLAYERS_CARDS_POSITION
from .color import colors_palet

def display_card(screen, point, color):
    a,b,c,d = point[0] - CARD_HALF_WHIDTH, point[1] - CARD_HALF_HIGHT, point[1] + CARD_HALF_HIGHT, point[0] + CARD_HALF_WHIDTH

    squer_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet[color], points=squer_point)

def display_back_infaction_card(screen, point=INFACTION_CARDS_POSITION):
    display_card(screen, point, 'DARK_GREEN')
    draw_biohazerd(screen, point, 'DARK_GREEN')    

def draw_biohazerd(screen, point, back_color, radius=25, symbol_color='SICK_GREEN'):
    #not supporting radius change
    a = point
    b = (a[0], a[1] - radius)    
    c = (a[0] + math.sqrt((3 * radius)), a[1]  + 0.5 * radius)    
    d = (a[0] - math.sqrt((3 * radius)), a[1]  + 0.5 * radius)  

    pygame.draw.circle(surface=screen, color=colors_palet[symbol_color], center=b , radius=1.2 * radius)
    pygame.draw.circle(surface=screen, color=colors_palet[symbol_color], center=c , radius=1.2 * radius)
    pygame.draw.circle(surface=screen, color=colors_palet[symbol_color], center=d , radius=1.2 * radius)
    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=a , radius=(0.5 *radius))

    e = (b[0], b[1] - 10)
    f = (c[0] + 15, c[1] + 15)
    g = (d[0] - 15, d[1] + 15)

    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=e , radius=0.8 * radius)
    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=f , radius=0.8 * radius)
    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=g , radius=0.8 * radius)



def display_back_players_card(screen, point=PLAYERS_CARDS_POSITION):
    display_card(screen, point, 'DARK_BLUE')
    draw_plas(screen, point)

def draw_plas(screen, point):
    HALF_HIGHT = 25
    HALF_WHIDTH = 75

    a,b,c,d = point[0] - HALF_WHIDTH, point[1] - HALF_HIGHT, point[1] + HALF_HIGHT, point[0] + HALF_WHIDTH
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['LIGHT_BLUE'], points=rectangle_point)

    a,b,c,d = point[0] - HALF_HIGHT, point[1] - HALF_WHIDTH, point[1] + HALF_WHIDTH, point[0] + HALF_HIGHT
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['LIGHT_BLUE'], points=rectangle_point)

def dispaly_front_player_card(screen, city, font, point=DISCARD_PLAYERS_CARDS_POSITION):
    dispaly_front_card(screen, point, city, font, city.color.name, 'GREEN')

def dispaly_front_infaction_card(screen, city, font, point=DISCARD_INFACTION_CARDS_POSITION):
    dispaly_front_card(screen, point, city, font, 'DARK_GREEN', city.color.name)

def dispaly_front_card(screen, point, city, font, background_color, text_color):
    display_card(screen, point, background_color)
    card_texts = ['city_name:', city.name, 'city_population:', city.population]
    point = (point[0] - 100, point[1] - 130)
    for text in card_texts:
        text_render = font.render(str(text), True, colors_palet[text_color])
        point = (point[0], point[1] + 30)
        screen.blit(text_render, point)