# Nathan Shulkin

# imports
import json

import premFunctions
import player

# set up data structures
teams = {}
xGlAst = {}
table = []
GATot = 0
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


table = premFunctions.displayTable(prem2021)

# add players to dictionary
xGlAst = premFunctions.getGoalsandAssists(prem2021, teams)

playersMW = {}
theMeaning = {}

# iterate through players and find ga for each matchweek
for person in xGlAst:
    for team in teams:
        if person[0] in teams[team]:
            playersMW[person[0]] = premFunctions.findGAInGame(prem2021, person[0], team)
    # print('')

print('\n\n')

# iterate through players and find meaning
for person in playersMW:
    for team in teams:
        if person in teams[team]:
            score, ptsScore, GATot, appMeaning, gaMeaning = premFunctions.findMeaning(prem2021, person, team, playersMW)
            theMeaning[person] = [score, ptsScore, GATot, appMeaning, gaMeaning]

# sort theMeaning
theMeaning = sorted(theMeaning.items(), key=lambda x: x[1], reverse=True)

print("player: meaningScr, meaningPts, totGA, meaningApp, meaningGA\n")
# display top 20
for i in range(0, 20):
    print(theMeaning[i])

