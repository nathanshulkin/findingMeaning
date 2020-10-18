# Nathan Shulkin

# functions


# display table
def displayTable(prem):
    # structure for table
    table = {}
    for team in prem:
        gd = 0
        points = 0
        for mw in prem[team]:
            # 3 points for a win
            if prem[team][mw]['result'] == 'w':
                points += 3
                gd += (prem[team][mw]['mScore'] - prem[team][mw]['oScore'])
            # 1 point for draw
            elif prem[team][mw]['result'] == 'd':
                points += 1
                gd += (prem[team][mw]['mScore'] - prem[team][mw]['oScore'])
            # nothing for a loss
            else:
                points += 0
                gd += (prem[team][mw]['mScore'] - prem[team][mw]['oScore'])
        # print(gd)
        # table[str(team)+'gd'] = gd
        table[team] = [points, gd]

    print('\n')
    # sort table
    table = sorted(table.items(), key=lambda x: x[1], reverse=True)
    for team in table:
        print(str(team[0]).capitalize() + ': ' + str(team[1][0]))


# display teams by mw
def displayTeamMW(prem, team, mw):
    print(team.upper() + ': ')
    print(str(prem[team][mw]['mScore']) + ' - ' + str(prem[team]['mw1']['oScore']))
    # check result of game
    if prem[team][mw]['result'] == 'w':
        print('win')
    elif prem[team][mw]['result'] == 'd':
        print('draw')
    else:
        print('loss')

    print('')

    print("goals:")  # + str(prem2021[team]['mw1']['goals']))
    for scor in prem[team][mw]['goals']:
        print(scor + ": " + str(prem[team]['mw1']['goals'][scor]) + "\t\t")
    print('')
    print("assists:")
    for astr in prem[team][mw]['assists']:
        print(astr + ": " + str(prem[team]['mw1']['assists'][astr]) + "\t\t")
    print('\n')


# display meaningful player
def displayMeaningfulPlayer(prem, player):
    print(player.upper() + ':')
    # pprint.pprint(prem1920[player])
    print('total: ' + str([prem[player]['totalGA']]) + '\t\tgoals: ' + str([prem[player]['g']]) + '\t\tassists: ' + str([prem[player]['a']]),
          '\nmeaningful goals+assists: ' + str([prem[player]['meaningfulGA']]),
          '\nmeaningful games with goal/assist: ' + str([prem[player]['meaningfulGame']]),
          '\npoints differential: ' + str([prem[player]['pointDif']]))
    print('\n')


# get goals and assists for players
def getGoalsandAssists(prem, teamsList):
    ga = {}

    # get goalers and assisters
    for team in prem:
        # for each matchweek
        for mw in prem[team]:
            # for each scorer
            for scorer in prem[team][mw]['goals']:
                # add scorer if they haven't scored/assisted before
                if scorer not in ga:
                    ga[scorer] = 0
                    teamsList[team].append(scorer)
                # add scorers goals to totals
                ga[scorer] = ga[scorer] + int(prem[team][mw]['goals'][scorer])
            # for each assister
            for assister in prem[team][mw]['assists']:
                # add assister if they haven't scored/assisted
                if assister not in ga:
                    ga[assister] = 0
                    teamsList[team].append(assister)
                # add assisters assist to totals
                ga[assister] = ga[assister] + int(prem[team][mw]['assists'][assister])

    # sort by most ga
    ga = sorted(ga.items(), key=lambda x: x[1], reverse=True)
    return ga


# find goals and assists for each matchweek
def findGAInGame(prem, player, team):

    # dictionary for each ga in each mw for player
    playerGA = {}

    # search through teams
    for daTeams in prem:
        # if player on team
        if team == daTeams:
            # for each mw for the team
            for mw in prem[daTeams]:
                # if player scored goal
                if player in prem[daTeams][mw]['goals']:
                    # add goals
                    try:
                        playerGA[str(mw)] += prem[daTeams][mw]['goals'][player]
                    # unless first goal
                    except KeyError:
                        playerGA[mw] = prem[daTeams][mw]['goals'][player]
                # if player assisted
                if player in prem[daTeams][mw]['assists']:
                    # add assists
                    try:
                        playerGA[str(mw)] += prem[daTeams][mw]['assists'][player]
                    # unless first assist
                    except KeyError:
                        playerGA[mw] = prem[daTeams][mw]['assists'][player]

    return playerGA


# find meaning for each player in each matchweek
def findMeaning(prem, player, team, playerGA):
    # variables to hold things
    totScore = 0
    totPtsScore = 0
    meaningApp = 0
    meaningGA = 0

    for daTeam in prem:
        if team == daTeam:
            for mw in playerGA[player]:
                result = prem[team][mw]['result']
                # print('')
                # print(result, end=" ")
                # print(str(prem[team][mw]['mScore']) + ' - ' + str(prem[team][mw]['oScore']))
                # print(player + ' scored/assisted', end=" ")
                # print(playerGA[player][mw])
                if result == 'w':
                    after = prem[team][mw]['mScore'] - playerGA[player][mw]
                    # print('after taking away ' + player + ' goals/assists: ')
                    # print(str(after) + ' - ' + str(prem[team][mw]['oScore']))
                    if after > prem[team][mw]['oScore']:
                        # print('meaningless goals')
                        int(1)
                    elif after == prem[team][mw]['oScore']:
                        # print('1 point for a tie | 1 point per goal')
                        totScore += 1
                        totPtsScore += playerGA[player][mw]
                        meaningApp += 1
                        meaningGA += playerGA[player][mw]
                    else:
                        # print('2 points for a win | 2 points per goal')
                        totScore += 2
                        totPtsScore += (2 * playerGA[player][mw])
                        meaningApp += 1
                        meaningGA += playerGA[player][mw]
                if result == 'd':
                    # print('1 point for a tie | 1 point per goal')
                    totScore += 1
                    totPtsScore += playerGA[player][mw]
                    meaningApp += 1
                    meaningGA += playerGA[player][mw]
                if result == 'l':
                    int(1)
                    # print('but they lost, so there is no meaning.')
                # print(totPtsScore)

    # print(str(player) + '\'s meaningful score: ' + str(totScore) + '\t\t\tmeaningful points score: ' + str(totPtsScore))

    return totScore, totPtsScore, meaningApp, meaningGA
