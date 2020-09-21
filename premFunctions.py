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
        print(scor + ": " + str(prem[team]['mw1']['goals'][scor]) + "\t\t", end="")
    print('')
    print("assists:")
    for astr in prem[team][mw]['assists']:
        print(astr + ": " + str(prem[team]['mw1']['assists'][astr]) + "\t\t", end="")
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


def findMeaningInGame(prem, player, team):
    # print('buttchug')
    # print(player.capitalize() + ' has ' + str(ga) + ' GA and is on ' + team)
    # dictionary for each ga in each mw for player
    playerGA = {}

    for daTeams in prem:
        if team == daTeams:
            for mw in prem[daTeams]:
                if player in prem[daTeams][mw]['goals']:
                    try:
                        playerGA[str(mw)] += prem[daTeams][mw]['goals'][player]
                    except KeyError:
                        playerGA[mw] = prem[daTeams][mw]['goals'][player]

                if player in prem[daTeams][mw]['assists']:
                    try:
                        playerGA[str(mw)] += prem[daTeams][mw]['assists'][player]
                    except KeyError:
                        playerGA[mw] = prem[daTeams][mw]['assists'][player]
            print(player.capitalize() + ': ')
            print(playerGA)

