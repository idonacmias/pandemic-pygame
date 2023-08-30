from display import BUTTON_WHIDTH, BUTTON_HIGHT



def click_on_botton(cities, players, corent_player, mouse_point):
    button_point = (500, 500)
    text = witch_click_on(mouse_point, button_point)
    


def witch_click_on(mouse_point, button_point):
    square_points = [button_point, (button_point[0] + BUTTON_WHIDTH, button_point[1] + BUTTON_HIGHT)]
    if is_in_squer(square_points, mouse_point):
        return text                 



def is_in_squer(square_points, point):
    x = 0
    y = 1
    return square_points[0][x] < point[x] and square_points[0][y] < point[y] and  square_points[1][x] > point[x] and square_points[1][y] > point[y]