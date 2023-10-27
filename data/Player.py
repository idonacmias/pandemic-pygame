from .constances import ACTION_PER_TURN
from random import randrange



class Player():

    players_roles = ['Quarantine_Specialist', #V  #no desisses cube in the neer by cities
                     'Dispatcher',            #V  #can move other player in his turn
                     'Operations_Expert',     #V  #can builed reserch station without card, can move anywere form reserch station by discarding card 
                     'Medic',                 #V  #treat all diseasse cube in city of the same color, treat diseasse with no action if cure is discoverd 
                     'Researcher',            #V  #can give his card, even if city shared is not the card thet move
                     'Scientist',             #V  #can discover cure with 4 card insted of 5
                     'Contingency_Planner']   #as an action can store on discard event card from discard player cards, and use it as evet

    def __init__(self, color, Player_cards, starter_city):
        self.color = color
        self.corent_city = starter_city
        self.actions = ACTION_PER_TURN
        self.hand = Player_cards
        self.role = 'Contingency_Planner' #players_roles[randrange(len(players_roles))]
        self.once_per_turn = True
        self.contingency_planner_event_card = None

