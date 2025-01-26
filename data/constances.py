FIRST_CITY = 'Atlanta'
ACTION_PER_TURN = 4
MAX_DISEASE_CUBE = 24
MAX_RESEARCH_STATION = 6
INFACTION_SCALE_CUNTER = [2, 2, 2, 3, 3, 4, 4]
NUM_PLAYERS_CARDS = [4, 3, 2]
NUMBER_CARDS_NEEDED_TO_CURE = 5
HAND_LIMIT = 7



players_roles = {'Quarantine_Specialist' : 'DARK_GREEN', #V  #no desisses cube in the neer by cities
                 'Dispatcher' : 'PURPLE',            #V  #can move other player in his turn
                 'Operations_Expert' : 'GREEN',     #V  #can builed reserch station without card, can move anywere form reserch station by discarding card 
                 'Medic' : 'ORENGE',                 #V  #treat all diseasse cube in city of the same color, treat diseasse with no action if cure is discoverd 
                 'Researcher' : 'BRAUN',            #V  #can give his card, even if city shared is not the card thet move
                 'Scientist' : 'WHITE',             #V  #can discover cure with 4 card insted of 5
                 'Contingency_Planner' : 'TEAL'}   #as an action can store on discard event card from discard player cards, and use it as evet
