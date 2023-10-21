from events import events_cards_events

names = ['one quiet night', 
         'resilient population',
         'forecast',
         'airlift',
         'government grant']

callback = [events_cards_events[key] for key in names]

description = ['skip the next infaction phase',
               'remove one card from infaction discard pile',
               'order the top 6 infaction cards',
               'move player freely on the map',
               'builed one free reserch station']

EVENTS_CARDS_ZIP = zip(callback, names, description)