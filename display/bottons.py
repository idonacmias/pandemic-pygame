from .Botton import Botton
from .constances import MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, MAP_BUTTONS_CALLBACKS_NAME
from .constances import CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS, CARDS_BUTTONS_CALLBACKS_NAME
from .constances import MAP_SMALL_BUTTONS_POINTS, MAP_SMALL_BUTTONS_TEXTS,  MAP_SMALL_CALLBACKS_NAME
from .constances import CARDS_SMALL_BUTTONS_POINTS, CARDS_SMALL_BUTTONS_TEXTS, CARDS_SMALL_CALLBACKS_NAME
from .constances import FORECAST_BUTTONS_POINTS, FORECAST_BUTTONS_TEXTS, FORECAST_BUTTONS_CALLBACKS_NAME
from .constances import RESILIENT_POPULATION_BUTTONS_POINTS, RESILIENT_POPULATION_BUTTONS_TEXTS, RESILIENT_POPULATION_BUTTONS_CALLBACKS_NAME
from .constances import BUTTON_WHIDTH, BUTTON_HIGHT, SMALL_BUTTON_WHIDTH, SMALL_BUTTON_HIGHT
from events import bottons_events

def create_bottons_list(points, texts, callbacks, whidth, hight):
   bottons_data = zip(points, texts, callbacks)
   bottons = [Botton(point[0], point[1], whidth, hight, text, bottons_events[callback]) for point, text, callback in bottons_data]
   return bottons    
   
def create_map_bottons():
   big_bottons = create_bottons_list(MAP_BUTTONS_POINTS, MAP_BUTTONS_TEXTS, MAP_BUTTONS_CALLBACKS_NAME, BUTTON_WHIDTH, BUTTON_HIGHT)
   small_bottons = create_bottons_list(MAP_SMALL_BUTTONS_POINTS, MAP_SMALL_BUTTONS_TEXTS, MAP_SMALL_CALLBACKS_NAME, SMALL_BUTTON_WHIDTH, SMALL_BUTTON_HIGHT)
   map_bottons = big_bottons + small_bottons
   return map_bottons


def create_cards_bottons():
   big_bottons = create_bottons_list(CARDS_BUTTONS_POINTS, CARDS_BUTTONS_TEXTS, CARDS_BUTTONS_CALLBACKS_NAME, BUTTON_WHIDTH, BUTTON_HIGHT)   
   small_bottons = create_bottons_list(CARDS_SMALL_BUTTONS_POINTS, CARDS_SMALL_BUTTONS_TEXTS, CARDS_SMALL_CALLBACKS_NAME, SMALL_BUTTON_WHIDTH, SMALL_BUTTON_HIGHT)
   cards_bottons = small_bottons + big_bottons
   return cards_bottons


def create_forecast_bottons():
   bottons = create_bottons_list(FORECAST_BUTTONS_POINTS, FORECAST_BUTTONS_TEXTS, FORECAST_BUTTONS_CALLBACKS_NAME, BUTTON_WHIDTH, BUTTON_HIGHT)   
   return bottons

def create_resilient_population_bottons():
   bottons = create_bottons_list(RESILIENT_POPULATION_BUTTONS_POINTS, RESILIENT_POPULATION_BUTTONS_TEXTS, RESILIENT_POPULATION_BUTTONS_CALLBACKS_NAME, BUTTON_WHIDTH, BUTTON_HIGHT)   
   return bottons

all_bottons ={'map' : create_map_bottons(),
              'cards' : create_cards_bottons(),
              'forecast' : create_forecast_bottons(),
              'resilient_population' : create_resilient_population_bottons()}
