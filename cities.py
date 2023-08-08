from City import City
import json

with open("cities.json", "r") as json_file:
  cities = json.load(json_file)

cities = {city["name"] : City(**city) for city in cities}
