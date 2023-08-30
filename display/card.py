import pygame
import math

from .constances import CARD_HALF_WHIDTH, CARD_HALF_HIGHT, INFACTION_CARDS_POSITION, DISCARD_INFACTION_CARDS_POSITION, DISCARD_PLAYERS_DECK_CARDS_POSITION, PLAYERS_DECK_CARDS_POSITION, SPACE_FROM_TOP, SPACE_BETWEEN_CARDS
from .color import colors_palet

from data import EventCard, City

def display_card_silhouette(screen, point, color):
    a,b,c,d = point[0] - CARD_HALF_WHIDTH, point[1] - CARD_HALF_HIGHT, point[1] + CARD_HALF_HIGHT, point[0] + CARD_HALF_WHIDTH

    squer_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet[color], points=squer_point)


def display_back_infaction_card(screen, point=INFACTION_CARDS_POSITION):
    display_card_silhouette(screen, point, 'DARK_GREEN')
    draw_biohazerd(screen, point, 'DARK_GREEN')    


def draw_biohazerd(screen, center_point, back_color, radius=25, symbol_color='SICK_GREEN'):
    #not supporting radius change
    radius_mod = [0.8]

    b = (center_point[0], center_point[1] - radius)    
    c = (center_point[0] + math.sqrt((3 * radius)), center_point[1]  + 0.5 * radius)    
    d = (center_point[0] - math.sqrt((3 * radius)), center_point[1]  + 0.5 * radius)  
    horn_circles_points = [b , c, d]
    radius_mod += [1.2] * 3

    e = (b[0], b[1] - 10)
    f = (c[0] + 15, c[1] + 15)
    g = (d[0] - 15, d[1] + 15)
    negative_horn_circles_points = [e , f, g]
    radius_mod += [0.8] * 3

    for horn_point in horn_circles_points:
        pygame.draw.circle(surface=screen, color=colors_palet[symbol_color], center=horn_point , radius=1.2 * radius)

    for horn_point in negative_horn_circles_points:
        pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=horn_point , radius=0.8 * radius)

    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=center_point , radius=(0.5 *radius))


def display_back_players_card(screen, point=PLAYERS_DECK_CARDS_POSITION):
    display_card_silhouette(screen, point, 'DARK_BLUE')
    draw_plas(screen, point)


def draw_plas(screen, point):
    HALF_HIGHT = CARD_HALF_HIGHT // 5
    HALF_WHIDTH = CARD_HALF_HIGHT // 1.5

    a,b,c,d = point[0] - HALF_WHIDTH, point[1] - HALF_HIGHT, point[1] + HALF_HIGHT, point[0] + HALF_WHIDTH
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['LIGHT_BLUE'], points=rectangle_point)

    a,b,c,d = point[0] - HALF_HIGHT, point[1] - HALF_WHIDTH, point[1] + HALF_WHIDTH, point[0] + HALF_HIGHT
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['LIGHT_BLUE'], points=rectangle_point)



def dispaly_front_infaction_card(screen, city, font, point=DISCARD_INFACTION_CARDS_POSITION):
    card_texts = city_card_text(city)
    dispaly_front_card(screen, point, city, font, 'DARK_GREEN', city.color.name, card_texts)


def dispaly_front_player_card(screen, player_card, font, point=DISCARD_PLAYERS_DECK_CARDS_POSITION):
    #match case   
    if is_card_of_type(player_card, City.City):
        card_texts = city_card_text(player_card)
        font_color = player_card.color.name
        background_color = 'GRAY'

    elif is_card_of_type(player_card, EventCard.EventCard):
        card_texts = event_card_text(player_card)
        font_color = 'GREEN'
        background_color = 'YELLOW'

    elif is_epidemic_card(player_card):
        card_texts = epidemic_card_text()
        font_color = 'BLACK'
        background_color = 'DARK_GREEN'

    dispaly_front_card(screen, point, player_card, font, font_color, background_color, card_texts)


def is_card_of_type(player_card, card_type):
    return type(player_card) == card_type
    #is_instance

def city_card_text(city):
    return ['city_name:', city.name, 'city_population:', city.population]


def event_card_text(event_card):
    return ['event_name:', event_card.name, event_card.description]


def dispaly_front_card(screen, point, city, font, background_color, text_color, card_texts):
    text_point = (point[0] - 100, point[1] - CARD_HALF_HIGHT)
    display_card_silhouette(screen, point, background_color)
    for text in card_texts:
        text_point = (text_point[0], text_point[1] + 30)
        display_text(screen, font, text, text_color, text_point)


def dispaly_players_cards(screen, font, cities, players, card_space_mod=0):
    space_from_side = 200 +  card_space_mod
    card_row = CARD_HALF_HIGHT * 2 + SPACE_BETWEEN_CARDS
    for player_num, player in enumerate(players):
        display_title(screen, font, card_row, player, player_num)
        display_player_hand(screen, font, player, card_row, player_num, space_from_side, cities)        


def display_title(screen, font, card_row, player, player_num):
    text_point = (100, card_row * player_num + 30)
    player_text = f'{player.color} in {player.corent_city_name}'
    display_text(screen, font, player_text, 'WHITE', text_point)



def display_player_hand(screen, font, player, card_row, player_num, space_from_side, cities):
    card_colom = CARD_HALF_WHIDTH * 2 + SPACE_BETWEEN_CARDS 
    for j, card in enumerate(player.hand):
        card_point = (space_from_side + j * card_colom, card_row * player_num + SPACE_FROM_TOP)
        dispaly_front_player_card(screen, cities[card], font, card_point)


def display_text(screen, font, text, text_color, point):
    text_render = font.render(str(text), True, colors_palet[text_color])
    screen.blit(text_render, point)

