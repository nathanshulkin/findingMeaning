# Nathan Shulkin

# functions
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


def displayMeaningfulPlayer(prem, player):
    print(player.upper() + ':')
    # pprint.pprint(prem1920[player])
    print('total: ' + str([prem[player]['totalGA']]) + '\t\tgoals: ' + str([prem[player]['g']]) + '\t\tassists: ' + str([prem[player]['a']]),
          '\nmeaningful goals+assists: ' + str([prem[player]['meaningfulGA']]),
          '\nmeaningful games with goal/assist: ' + str([prem[player]['meaningfulGame']]),
          '\npoints differential: ' + str([prem[player]['pointDif']]))
    print('\n')


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


def findMeaning(prem, player, team, playerGA):
    # variables to hold things
    result = ''
    after = 0
    totScore = 0
    totPtsScore = 0

    for daTeam in prem:
        if team == daTeam:
            for mw in playerGA[player]:
                result = prem[team][mw]['result']
                print('')
                print(result, end=" ")
                print(str(prem[team][mw]['mScore']) + ' - ' + str(prem[team][mw]['oScore']))
                print(player + ' scored/assisted', end=" ")
                print(playerGA[player][mw])
                if result == 'w':
                    after = prem[team][mw]['mScore'] - playerGA[player][mw]
                    print('after taking away ' + player + ' goals/assists: ')
                    print(str(after) + ' - ' + str(prem[team][mw]['oScore']))
                    if after > prem[team][mw]['oScore']:
                        print('meaningless goals')
                    elif after == prem[team][mw]['oScore']:
                        print('1 point for a tie | 1 point per goal')
                        totScore += 1
                        totPtsScore += playerGA[player][mw]
                    else:
                        print('2 points for a win | 2 points per goal')
                        totScore += 2
                        totPtsScore += totPtsScore + (2 * playerGA[player][mw])
                if result == 'd':
                    after = prem[team][mw]['mScore'] - playerGA[player][mw]
                    print('after taking away ' + player + ' goals/assists: ' + str(after))
                    print('1 point for a tie | 1 point per goal')
                    totScore += 1
                    totPtsScore += playerGA[player][mw]
                if result == 'l':
                    print('')
                    print('but they lost, so there is no meaning.')

    print('')
    print(str(player) + '\'s meaningful score: ' + str(totScore) + '\t\t\tmeaningful points score: ' + str(totPtsScore))

    return totScore, totPtsScore
