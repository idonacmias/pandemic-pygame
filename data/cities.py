import json

from .City import City



def crate_cities():
  with open("data/cities.json", "r") as json_file:
    cities = json.load(json_file)

  cities = {city["name"] : City(**city) for city in cities}
  return cities