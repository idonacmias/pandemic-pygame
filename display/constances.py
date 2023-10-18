CITY_RADIUS = 25
EDGE_CITIES = ['San Francisco', 'Los Angeles', 'Sydney', 'Manila', 'Tokyo']
RESEARCH_STATION_RADIUS = 10


INFACTION_CARDS_POSITION = (1400, 150)
DISCARD_INFACTION_CARDS_POSITION = (1700, 150)


PLAYERS_DECK_POSITION = (1200, 950)
DISCARD_PLAYERS_DECK_POSITION = (1450, 950)
CARD_HALF_HIGHT = 90
CARD_HALF_WHIDTH = 100


INFACTION_SCALE_POSITIONS = [(i, 300) for i in range(1200, 1900, 100)]

BAR_CIRCLE_RADIUS = 20

CURE_BAR_POINT = [(i, 950) for i in range(600, 1000, 100)]
OUTBREAK_BAR_POINTS = [(100, 600), (200, 650), (100, 700), (200, 750), (100, 800), (200, 850), (100, 900), (200, 950), (100, 1000)]

MAP_BUTTONS_POINTS = [(250, 920), (250, 970)]
MAP_BUTTONS_TEXTS = ['builed research station', 'display player cards']
MAP_BUTTONS_CALLBACKS_NAME = ['builed_research_station', 'switch_bord_to_cards']

MAP_SMALL_BUTTONS_POINTS = [(600, 1020), (700, 1020), (800, 1020), (900, 1020)]
MAP_SMALL_BUTTONS_TEXTS = ['blue', 'yellow', 'black', 'red']
MAP_SMALL_CALLBACKS_NAME = ['cure_blue', 'cure_yellow', 'cure_black', 'cure_red']


CARDS_BUTTONS_POINTS = [(250, 970), (250, 1020), (1250, 970), (1250, 1020)]
CARDS_BUTTONS_TEXTS = ['back to map', 'direct flight', 'discover cure', 'share knowledge']
CARDS_BUTTONS_CALLBACKS_NAME = ['switch_bord_to_map', 'direct_flight', 'discover_cure', 'share_knowledge']

CARDS_SMALL_BUTTONS_POINTS = [(600, 1020), (700, 1020), (800, 1020), (900, 1020)]
CARDS_SMALL_BUTTONS_TEXTS = ['player 1', 'player 2', 'player 3', 'player 4']
CARDS_SMALL_CALLBACKS_NAME = ['player 1', 'player 2', 'player 3', 'player 4']


BUTTON_HIGHT = 25
BUTTON_WHIDTH = 225

SMALL_BUTTON_HIGHT = 25
SMALL_BUTTON_WHIDTH = 70


SPACE_BETWEEN_CARDS = 50
SPACE_FROM_TOP = 150