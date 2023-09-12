from display import CARD_HALF_HIGHT, SPACE_BETWEEN_CARDS, culculate_cards_point, culculate_card_square, CARD_HALF_WHIDTH, CARD_HALF_HIGHT



def click_on_botton(cities, players, corent_player, botton_clicked):
    if botton_clicked == 'back to map':
        corent_page = 'map'
        return corent_page 

    elif botton_clicked == 'share knowledge':
        print('share knowledge')
        share_knowledge(corent_player)

    elif botton_clicked == 'discover cure':
        pass


def share_knowledge(corent_player):
    NUM_CARDS_FOR_CURE = 5
    cards = chose_cards(NUM_CARDS_FOR_CURE)
    if is_cure_verifie(cards):
        player_discard_cards(cards)
        cure_update()
        player_loose_action()


def cards_points(players, card_space_mod=0):
    space_from_side = 200 +  card_space_mod
    card_row = CARD_HALF_HIGHT * 2 + SPACE_BETWEEN_CARDS
    player_cards_points = []
    for player_num, player in enumerate(players):
        player_cards_points += culculate_cards_point(player, card_row, player_num, space_from_side)

    return player_cards_points


def witch_card_click_on(mouse_point, players):
    cards_data = cards_points(players)
    for card_point, card in cards_data: 
        square_points = culculate_card_square(card_point)
        square_points = [square_points[0], square_points[2]]
        if is_in_squer(square_points, mouse_point):
            return card                 


def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]