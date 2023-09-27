from display import CARD_HALF_HIGHT, SPACE_BETWEEN_CARDS, culculate_cards_point, culculate_card_square, CARD_HALF_WHIDTH, CARD_HALF_HIGHT
from lib import discover_cure


def click_on_botton(bord_state, cities, corent_player, botton_clicked, picked_cards):
    corent_page = None
    if botton_clicked == 'back to map':
        corent_page = 'map' 

    elif botton_clicked == 'share knowledge':
        print('share knowledge')
        share_knowledge(corent_player)

    elif botton_clicked == 'discover cure':
        print(picked_cards)
        picked_cards = discover_cure(bord_state, picked_cards, corent_player)
        print(picked_cards)

    return corent_page, picked_cards

def share_knowledge(corent_player):
    NUM_CARDS_FOR_CURE = 5
    cards = chose_cards(NUM_CARDS_FOR_CURE)
    if is_cure_verifie(cards):
        player_discard_cards(cards)
        cure_update()
        player_loose_action()


def witch_card_click_on(mouse_point, players, picked_cards):
    cards_data = cards_points(players)
    for card_point, card in cards_data: 
        square_points = culculate_card_square(card_point)
        square_points = [square_points[0], square_points[2]]
        if is_in_squer(square_points, mouse_point):
            for i, prev_picked_card in enumerate(picked_cards):
                if prev_picked_card == card:
                    picked_cards.pop(i)
                    break

            else:
                picked_cards.append(card)
            
            print(picked_cards)
            return picked_cards                 

    return picked_cards

def cards_points(players, card_space_mod=0):
    space_from_side = 200 +  card_space_mod
    card_row = CARD_HALF_HIGHT * 2 + SPACE_BETWEEN_CARDS
    player_cards_points = []
    for player_num, player in enumerate(players):
        player_cards_points += culculate_cards_point(player, card_row, player_num, space_from_side)

    return player_cards_points


def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]


# def clicked_on_player(mouse_point):
#     player_points = [(0,0),(2000, 2000)]
#     if is_in_squer(player_points, mouse_point):
#         print(player)

#     return player    