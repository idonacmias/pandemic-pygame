import pygame
import sys
import math

from color import colors_palet
from cities import cities

from constances import CITY_RADIUS, INFACTION_CARDS_POSITION, DISCARD_INFACTION_CARDS_POSITION, PLAYERS_CARDS_POSITION, DISCARD_PLAYERS_CARDS_POSITION



def main(cities):
    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill(colors_palet['PURPLE'])
    city_font = pygame.font.Font(None, 28) 
    # screen.image.load('')
    clock = pygame.time.Clock()
    corent_city = set_bord(screen, city_font)
    display_back_infaction_card(screen, INFACTION_CARDS_POSITION)
    display_card(screen, DISCARD_INFACTION_CARDS_POSITION, 'DARK_GREEN')
    display_back_players_card(screen, PLAYERS_CARDS_POSITION)
    display_card(screen, DISCARD_PLAYERS_CARDS_POSITION, 'WHITE')
    # draw_biohazerd(screen, (500, 500), 'PURPLE')
    while True:
        for event in pygame.event.get():
            if_quit(event)
            corent_city = clicked_on_city(event, cities, screen, corent_city, city_font)

        pygame.display.update()
        clock.tick(60)

def set_bord(screen, city_font):
    for city in cities.values():
        city.draw(screen, colors_palet[city.color.name], city_font)
        
        other_city = cities[city.routes[0]]
        for other_city_name in city.routes:
            other_city = cities[other_city_name]
            pygame.draw.line(screen, colors_palet['PINK'], city.point, other_city.point, 2)

    FIRST_CITY = 'Atlanta'
    corent_city = cities[FIRST_CITY]
    corent_city.resarch_station = True
    corent_city.draw(screen, colors_palet['PINK'], city_font)
    return corent_city

def display_back_players_card(screen, point):
    display_card(screen, point, 'DARK_BLUE')
    display_plas(screen, point)

def display_card(screen, point, color):
    HALF_HIGHT = 122
    HALF_WHIDTH = 100
    a,b,c,d = point[0] - HALF_WHIDTH, point[1] - HALF_HIGHT, point[1] + HALF_HIGHT, point[0] + HALF_WHIDTH

    squer_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet[color], points=squer_point)

def display_plas(screen, point):
    HALF_HIGHT = 25
    HALF_WHIDTH = 75
    a,b,c,d = point[0] - HALF_WHIDTH, point[1] - HALF_HIGHT, point[1] + HALF_HIGHT, point[0] + HALF_WHIDTH

    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['LIGHT_BLUE'], points=rectangle_point)

    a,b,c,d = point[0] - HALF_HIGHT, point[1] - HALF_WHIDTH, point[1] + HALF_WHIDTH, point[0] + HALF_HIGHT
    rectangle_point = [(a, b), (a, c), (d, c), (d, b)]
    pygame.draw.polygon(surface=screen, color=colors_palet['LIGHT_BLUE'], points=rectangle_point)

def display_back_infaction_card(screen, point):
    display_card(screen, point, 'DARK_GREEN')
    draw_biohazerd(screen, point, 'DARK_GREEN')    

def draw_biohazerd(screen, point, back_color, radius=25):
    a = point
    b = (a[0], a[1] - radius)    
    c = (a[0] + math.sqrt((3 * radius)), a[1]  + 0.5 * radius)    
    d = (a[0] - math.sqrt((3 * radius)), a[1]  + 0.5 * radius)  
    print(f'a: {a}\nb: {b}\nc: {c}\nd: {d}\n')

    pygame.draw.circle(surface=screen, color=colors_palet['SICK_GREEN'], center=b , radius=30)
    pygame.draw.circle(surface=screen, color=colors_palet['SICK_GREEN'], center=c , radius=30)
    pygame.draw.circle(surface=screen, color=colors_palet['SICK_GREEN'], center=d , radius=30)
    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=a , radius=(0.5 *radius))

    e = (b[0], b[1] - 10)
    f = (c[0] + 15, c[1] + 15)
    g = (d[0] - 15, d[1] + 15)

    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=e , radius=20)
    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=f , radius=20)
    pygame.draw.circle(surface=screen, color=colors_palet[back_color], center=g , radius=20)

def if_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def clicked_on_city(event, cities, screen, corent_city, city_font):
    if event.type == pygame.MOUSEBUTTONUP:
        muose_point = pygame.mouse.get_pos()
        min_radius = CITY_RADIUS
        closest_city = None

        for city_name in corent_city.routes:
            city = cities[city_name]
            temp_min_radius = city.click_lenth_from_center(muose_point)
            if temp_min_radius <= min_radius:
                min_radius = temp_min_radius
                closest_city = city


        if closest_city:
            closest_city.draw(screen, colors_palet['PINK'], city_font)
            corent_city.draw(screen, colors_palet[corent_city.color.name], city_font)
            return closest_city 

    return corent_city

if __name__ == '__main__':

    main(cities)











        # text and label in pygame 
        # city_font = pygame.font.Font(None, 36) 

        # text = "Hello, Pygame!"
        
        # text_surface = city_font.render(text, True, (255, 255, 255))  # White color

        # # Blit the text surface onto the screen at position (x, y)
        # x, y = 50, 50

        # screen.blit(text_surface, (x, y))
