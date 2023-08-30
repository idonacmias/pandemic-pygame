from display import BUTTON_WHIDTH, BUTTON_HIGHT, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS



def click_on_botton(cities, players, corent_player, mouse_point):
    buttons_data = zip(CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS)
    botton_clicked = witch_click_on(mouse_point, buttons_data)
    if botton_clicked == 'back to map':
        corent_page = 'map'
        return corent_page 


def witch_click_on(mouse_point, buttons_data):
    for button_point, text in buttons_data:   
        square_points = [button_point, (button_point[0] + BUTTON_WHIDTH, button_point[1] + BUTTON_HIGHT)]
        if is_in_squer(square_points, mouse_point):
            return text                 



def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]