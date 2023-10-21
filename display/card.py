import pygame
import math

from .color import colors_palet
from .constances import INFACTION_CARDS_POSITION, DISCARD_INFACTION_CARDS_POSITION, PLAYERS_DECK_POSITION, DISCARD_PLAYERS_DECK_POSITION



def dispaly_players_cards(screen, font, players):
    for i, player in enumerate(players):
        y = i * 250 + 100
        for j, card in enumerate(player.hand):
            x = (j + 1) * 250
            card.center = (x, y)
            card.draw(screen, font)


def display_infaction_discard_card(screen, font, bord_state):
    if bord_state.infaction_discard_cards:
        infaction_card = bord_state.infaction_discard_cards[-1]
        infaction_card.center = DISCARD_INFACTION_CARDS_POSITION
        infaction_card.draw(screen, font)

    else:
        display_empty_card(screen, DISCARD_INFACTION_CARDS_POSITION)


def display_player_discard_card(screen, font, bord_state):
    if bord_state.player_discard_cards: 
      card = bord_state.player_discard_cards[-1]
      card.center = DISCARD_PLAYERS_DECK_POSITION
      card.draw(screen, font)

    else:
        display_empty_card(screen, DISCARD_PLAYERS_DECK_POSITION)

def display_empty_card(screen, center):
    card = pygame.Rect(0, 0, 180, 200)
    card.center = center
    pygame.draw.rect(screen, colors_palet['WHITE'], card)

def display_back_infaction_card(screen):
    back_color = 'GREEN'
    back_infaction_card = pygame.Rect(0, 0, 180, 200)
    back_infaction_card.center = INFACTION_CARDS_POSITION
    pygame.draw.rect(screen, colors_palet[back_color], back_infaction_card)
    center_point = back_infaction_card.center
    draw_biohazerd(screen, center_point, back_color)


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


def display_back_players_card(screen):
    back_color = 'DARK_BLUE'
    back_infaction_card = pygame.Rect(0, 0, 180, 200)
    back_infaction_card.center = PLAYERS_DECK_POSITION
    pygame.draw.rect(screen, colors_palet[back_color], back_infaction_card)
    center_point = back_infaction_card.center
    draw_plas(screen, center_point)


def draw_plas(screen, point):
    HIGHT = 180 // 5
    WHIDTH = 200 // 1.5
    horizontal_line = pygame.Rect(0, 0,WHIDTH,  HIGHT)
    Vertical_line = pygame.Rect(0, 0,  HIGHT, WHIDTH)
    
    horizontal_line.center = point
    Vertical_line.center = point

    pygame.draw.rect(screen, colors_palet['LIGHT_BLUE'], horizontal_line)
    pygame.draw.rect(screen, colors_palet['LIGHT_BLUE'], Vertical_line)

