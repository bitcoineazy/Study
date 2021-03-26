import requests
from pprint import pprint





all_characters = requests.get('https://swapi.dev/api/people/').json()['results']
luke = requests.get('https://swapi.dev/api/people/?search=Luke').json()['results'][0]
homeworld = luke['homeworld']
planet = requests.get(homeworld)
diameter = planet.json()['diameter']
pprint(int(diameter))