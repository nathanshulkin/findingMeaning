# Nathan Shulkin

# imports
import json

import premFunctions
from player import *

# set up data structures
teams = {}
xGlAst = {}
xGoals = {}
xAssists = {}
goalsANDassists= {}
table = []
daPlayers = []
GATot = 0
ptDiff = 0
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
tableLast10 = premFunctions.displayTableLast10(prem2021)

# add players to dictionary
xGlAst, xGoals, xAssists = premFunctions.getGoalsandAssists(prem2021, teams)


for g in xGoals:
    goalsANDassists[g[0]] = [g[1], 0]
for a in xAssists:
    try:
        goalsANDassists[a[0]][1] = a[1]
    except KeyError:
        goalsANDassists[a[0]] = [0, a[1]]
for i in goalsANDassists:
    print(i, end=" ")
    print(goalsANDassists[i])

playersMW = {}

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
            score, ptsScore, GATot, appMeaning, gaMeaning, ptDiff, ptContribute = premFunctions.findMeaning(prem2021, person, team, playersMW)
            # create players
            daPlayers.append(Player(person, goalsANDassists[person][0], goalsANDassists[person][1], gaMeaning,
                                    appMeaning, score, ptsScore, ptDiff, ptContribute, team))

# sort theMeaning
daPlayers = sorted(daPlayers, key=lambda x: x.getGA(), reverse=True)

