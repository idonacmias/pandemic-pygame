from .Label import Label 
from .constances import LABEL_HIGHT, LABEL_WHIDTH, SMALL_LABEL_WHIDTH, SMALL_LABEL_HIGHT
from .constances import WIN_LABEL_POINTS, WIN_LABEL_TEXTS, WIN_TEXT_COLOR, WIN_BACKRAOND_COLOR
from .constances import LOSE_LABEL_POINTS, LOSE_LABEL_TEXTS, LOSE_TEXT_COLOR, LOSE_BACKRAOND_COLOR
from .constances import MAP_LABEL_POINTS, MAP_LABEL_TEXTS, MAP_TEXT_COLOR, MAP_BACKRAOND_COLOR 
from .constances import CREATE_COSTUM_LABEL_POINTS, CREATE_COSTUM_LABEL_TEXTS, CREATE_COSTUM_TEXT_COLOR, CREATE_COSTUM_BACKRAOND_COLOR
from .constances import SMALL_CREATE_COSTUM_LABEL_POINTS, SMALL_CREATE_COSTUM_LABEL_TEXTS, SMALL_CREATE_COSTUM_TEXT_COLOR, SMALL_CREATE_COSTUM_BACKRAOND_COLOR

def create_labels_list(points, texts, backraond_color, text_color, whidth, hight):
   label_data = zip(points, texts, backraond_color, text_color)
   labels = [Label(point[0], point[1], whidth, hight, text, backraond_color, text_color) for point, text, backraond_color, text_color in label_data]
   return labels   

   
def create_win_labels():
   labels = create_labels_list(WIN_LABEL_POINTS, WIN_LABEL_TEXTS, WIN_BACKRAOND_COLOR, WIN_TEXT_COLOR, LABEL_WHIDTH, LABEL_HIGHT)
   return labels


def create_lose_labels():
    labels = create_labels_list(LOSE_LABEL_POINTS, LOSE_LABEL_TEXTS, LOSE_TEXT_COLOR, LOSE_BACKRAOND_COLOR, LABEL_WHIDTH, LABEL_HIGHT)
    return labels


def create_map_labels():
    labels = create_labels_list(MAP_LABEL_POINTS, MAP_LABEL_TEXTS, MAP_TEXT_COLOR, MAP_BACKRAOND_COLOR, LABEL_WHIDTH, LABEL_HIGHT)
    return labels


def create_costum_game_labels():
    big_labels = create_labels_list(CREATE_COSTUM_LABEL_POINTS, CREATE_COSTUM_LABEL_TEXTS, CREATE_COSTUM_TEXT_COLOR, CREATE_COSTUM_BACKRAOND_COLOR, LABEL_WHIDTH, LABEL_HIGHT)
    small_labels = create_labels_list(SMALL_CREATE_COSTUM_LABEL_POINTS, SMALL_CREATE_COSTUM_LABEL_TEXTS, SMALL_CREATE_COSTUM_TEXT_COLOR, SMALL_CREATE_COSTUM_BACKRAOND_COLOR, SMALL_LABEL_WHIDTH, SMALL_LABEL_HIGHT)
    labels =  small_labels + big_labels
    return labels
    

all_labels ={'win' : create_win_labels(),
             'lose' : create_lose_labels(),
             'map' : create_map_labels(),
             'costum_game' : create_costum_game_labels()}

