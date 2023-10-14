from .Botton import Botton
from .constances import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, MAP_BUTTONS_CALLBACKS_NAME, CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS, MAP_SMALL_BUTTONS_POINTS, MAP_SMALL_BUTTONS_TEXTS, BUTTON_WHIDTH, BUTTON_HIGHT, SMALL_BUTTON_WHIDTH, SMALL_BUTTON_HIGHT, MAP_SMALL_CALLBACKS_NAME, CARDS_BUTTONS_CALLBACKS_NAME
from events import user_events

def create_buttons_list(points, texts, callbacks, whidth, hight):
   buttons_data = zip(points, texts, callbacks)
   bottons = [Botton(point[0], point[1], whidth, hight, text, user_events[callback]) for point, text, callback in buttons_data]
   return bottons    
   
def create_map_bottons():
   big_bottons = create_buttons_list(MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, MAP_BUTTONS_CALLBACKS_NAME, BUTTON_WHIDTH, BUTTON_HIGHT)
   small_bottons = create_buttons_list(MAP_SMALL_BUTTONS_POINTS, MAP_SMALL_BUTTONS_TEXTS, MAP_SMALL_CALLBACKS_NAME, SMALL_BUTTON_WHIDTH, SMALL_BUTTON_HIGHT)
   map_bottons = big_bottons + small_bottons
   return map_bottons


def create_cards_bottons():
   cards_bottons = create_buttons_list(CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS, CARDS_BUTTONS_CALLBACKS_NAME, BUTTON_WHIDTH, BUTTON_HIGHT)   
   return cards_bottons



all_buttons ={'map' : create_map_bottons(),
              'cards' : create_cards_bottons()}
