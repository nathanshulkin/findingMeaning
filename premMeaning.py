# Nathan Shulkin

# imports
import json

import premFunctions

# set up data structures
teams = {}
xGlAst = {}
global prem1920
global prem2021

# open files, read in json data
with open("prem1920.json", 'r') as premSon:
    prem1920 = json.load(premSon)

with open("prem2021.json", 'r') as premSon:
    prem2021 = json.load(premSon)

# get list of prem teams
for team in prem2021:
    teams[team] = []

# get matchweek
mchwek = "mw" + str(input("what matchweek would you like? "))

for teem in teams:
    try:
        premFunctions.displayTeamMW(prem2021, teem, mchwek)
        print('\n')
    except KeyError:
        print('have not played ' + mchwek + ' yet\n\n')
print('\n\n\n')

# iterate through and display player info
# for plyr in prem1920:
    # premFunctions.displayMeaningfulPlayer(prem1920, plyr)

# add players to dictionary
xGlAst = premFunctions.getGoalsandAssists(prem2021, teams)


# iterate through players and find meaning
for person in xGlAst:
    for team in teams:
        if person[0] in teams[team]:
            premFunctions.findMeaningInGame(prem2021, person[0], team)
    # print('')

