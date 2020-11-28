# Nathan Shulkin
# meaning in the champions league

# imports
import json

import premFunctions
from player import *

import premFunctions

teams = {}
# open files, read in json data
with open("chLg.json", 'r') as chSon:
    chLg20 = json.load(chSon)

for team in chLg20:
    print(team)
