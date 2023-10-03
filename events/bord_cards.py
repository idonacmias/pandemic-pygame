from display import CARD_HALF_HIGHT, SPACE_BETWEEN_CARDS, culculate_cards_point, culculate_card_square, CARD_HALF_WHIDTH, CARD_HALF_HIGHT, culculate_card_row, culculate_player_point
from lib import discover_cure, share_knowledge


def click_on_botton(bord_state, corent_player, botton_clicked, picked_cards, picked_player):
    corent_page = None
    if botton_clicked == 'back to map':
        corent_page = 'map' 

    elif botton_clicked == 'share knowledge':
        share_knowledge(corent_player, picked_player, picked_cards)
        picked_cards = []
        picked_player = None

    elif botton_clicked == 'discover cure':
        discover_cure(bord_state, picked_cards, corent_player)
        picked_cards = []
    
    return corent_page, picked_cards, picked_player


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


def clicked_on_player(mouse_point, piked_player, players):
    players_points = []
    card_row = culculate_card_row()
    for i in range(len(players)):
        player_point = culculate_player_point(card_row, i)
        player_squer_points = [player_point, [player_point[0] + 5000, player_point[1] + 100]]
        players_points.append(player_squer_points)

    for i, player_points in enumerate(players_points):
        if is_in_squer(player_points, mouse_point):
            piked_player = players[i]

    return piked_player