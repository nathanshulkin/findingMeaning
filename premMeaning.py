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
# mchwek = "mw" + str(input("what matchweek would you like? "))

# for teem in teams:
    # try:
        # premFunctions.displayTeamMW(prem2021, teem, mchwek)
        # print('\n')
    # except KeyError:
        # print('have not played ' + mchwek + ' yet\n\n')
# print('\n\n\n')

# iterate through and display player info
# for plyr in prem1920:
    # premFunctions.displayMeaningfulPlayer(prem1920, plyr)


premFunctions.displayTable(prem2021)

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

print('players who have scored or assisted in the prem in 20/21...\n\n')

# iterate through players and find meaning
for person in playersMW:
    for team in teams:
        if person in teams[team]:
            print(person.capitalize())
            score, ptsScore, appMeaning, gaMeaning = premFunctions.findMeaning(prem2021, person, team, playersMW)
            theMeaning[person] = [score, ptsScore, appMeaning, gaMeaning]

print('\n\n')

# sort theMeaning
theMeaning = sorted(theMeaning.items(), key=lambda x: x[1], reverse=True)

print("player: meaningScr, meaningPts, meaningApp, meaningGA\n")
# display top 20
for i in range(0, 20):
    print(theMeaning[i])

