# Nathan Shulkin
# show some prem stuff using plotly

# pip install plotly
from plotly import offline

import premMeaning as pm


# define some data
meanApp = []
meanGA = []
meanScore = []
meanPoints = []
meaningfulGApGame = []
goals = []
assists = []
totGA = []
players = []
team = []
points = []
teamPlayed = []
teamGD = []
teamGS = []
teamGA = []
ptDiff = []
ptContributed = []
playerTeam = []
teamLast10 = []
pointsLast10 = []
teamGDLast10 = []

# get the data
for i in range(len(pm.daPlayers)):
    meanScore.append(pm.daPlayers[i].getMeanScore())
    meanPoints.append(pm.daPlayers[i].getMeanPoints())
    meanApp.append(pm.daPlayers[i].getMeanApp())
    meanGA.append(pm.daPlayers[i].getMeanGA())
    totGA.append(pm.daPlayers[i].getGA())
    ptDiff.append(pm.daPlayers[i].getPointDiff())
    ptContributed.append((pm.daPlayers[i].getPointContribute()))
    playerTeam.append(pm.daPlayers[i].getTeam())
    try:
        meaningfulGApGame.append(pm.daPlayers[i].getMeanGA()/pm.daPlayers[i].getMeanApp())
    except ZeroDivisionError:
        meaningfulGApGame.append(0)
    players.append(pm.daPlayers[i].getName())

    try:
        team.append(pm.table[i][0])
        points.append(pm.table[i][1][0])
        teamGD.append(pm.table[i][1][1])
        teamGS.append(pm.table[i][1][3])
        teamGA.append(pm.table[i][1][4])
        teamPlayed.append(pm.table[i][1][2])
        teamLast10.append(pm.tableLast10[i][0])
        pointsLast10.append(pm.tableLast10[i][1][0])
        teamGDLast10.append(pm.tableLast10[i][1][1])
    except IndexError:
        True

    goals.append(pm.daPlayers[i].getGoals())
    assists.append(pm.daPlayers[i].getAssists())


players.reverse()
goals.reverse()
assists.reverse()
totGA.reverse()
meanGA.reverse()
meanApp.reverse()
meanScore.reverse()
meanPoints.reverse()
meaningfulGApGame.reverse()
ptDiff.reverse()
ptContributed.reverse()
playerTeam.reverse()

points.reverse()
team.reverse()
pointsLast10.reverse()
teamLast10.reverse()

# scatter plot, color gradient

# meaning in the prem
scatterData = [{
    'type': 'scatter',
    'x': totGA[-25:],
    'y': meanGA[-25:],
    'text': players[-25:],
    'mode': 'markers+text',
    'hoverinfo': 'text+x+y',
    'textposition': 'top center',
    # 'size': 10,
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
    }]

# layout as dictionary/json for graph object
scatLayout = {
    'title': 'Meaning in the Prem 20/21',
    'xaxis': {
        'title': 'Total Goals/Assists',
        'range': [0, 35]
    },
    'yaxis': {
        'title': 'Meaningful Goals/Assists',
        'range': [0, 25]
    },
    'template': 'plotly_dark'

}


# unzip dictionary into two tuples
# thisList = goals.items()
# scorers, goalNum = zip(*thisList)

# goals + assists
# total
# bar
goalBars = [{
    'type': 'bar',
    'x': goals[-22:],
    'y': players[-22:],
    'name': 'goals',
    'width': 0.5,
    'orientation': 'h',
    'marker_color': 'indigo'
    },

    {
    'type': 'bar',
    'x': assists[-22:],
    'y': players[-22:],
    'name': 'assists',
    'width': 0.5,
    'orientation': 'h',
    'marker_color': 'mediumpurple'
    }]

# layout
gaBarLayout = {
    'title': 'Goals and Assists in the Premier League 20/21',
    'xaxis': {
        'title': '',
        'tickmode': 'linear',
    },
    'yaxis': {
        # 'tickmode': 'linear',
    },
    'barmode': 'stack',
    'template': 'plotly_dark'

}


# total
# scatter
goalScatter = [{
    'type': 'scatter',
    'x': goals[-30:],
    'y': assists[-30:],
    'text': players[-30:],
    'mode': 'markers+text',
    'hoverinfo': 'text+x+y',
    'textposition': 'top center',
    # 'size': '10',
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
}]

# layout
gaScatLayout = {
    'title': 'Goals and Assists in the Prem 20/21',
    'xaxis': {
        'title': 'Goals',
        'tickmode': 'linear',
        'range': [0, 20]
    },
    'yaxis': {
        'title': 'Assists',
        'tickmode': 'linear',
        'range': [0, 20]
    },
    'template': 'plotly_dark'

}

# meaningful GAs vs meaningful apps
barData = [{
    'type': 'bar',
    'x': players[-22:],
    'y': meanGA[-22:],
    'name': 'meaningful goals/assists',
    'width': 0.5,
    'marker_color': 'mediumpurple'
    },

    {
    'type': 'bar',
    'x': players[-22:],
    'y': meanApp[-22:],
    'name': 'meaningful appearances',
    'width': 0.5,
    'marker_color': 'gold'
    }]

# layout
barLayout = {
    'title': 'Meaning in the Premier League 20/21',
    'xaxis': {
        'title': '',
    },
    'yaxis': {
        'tickmode': 'linear',
    },
    'template': 'plotly_dark'

}


# points contributed for goal/assits contributions
# scatter
ptContScat = [{
    'type': 'scatter',
    'x': players[-40:],
    'y': ptContributed[-40:],
    'text': ptContributed[-40:],
    'mode': 'markers+text',
    'hoverinfo': 'text+x',
    'textposition': 'top center',
    # 'size': '10',
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
}]

ptContLayout = {
    'title': 'Points Conrtributed Prem Players 20/21',
    'xaxis': {
        'title': '',
    },
    'yaxis': {

    },
    'template': 'plotly_dark'

}


# point differentials for goal contributions
# scatter
ptDiffScat = [{
    'type': 'scatter',
    'x': players[-40:],
    'y': ptDiff[-40:],
    'text': ptDiff[-40:],
    'mode': 'markers+text',
    'hoverinfo': 'text+x',
    'textposition': 'top center',
    # 'size': '10',
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
}]

ptDiffLayout = {
    'title': 'Point Differentials Prem Players 20/21',
    'xaxis': {
        'title': '',
    },
    'yaxis': {
        'tickmode': 'linear',
    },
    'template': 'plotly_dark'

}


# prem table
premTable = {
    'type': 'bar',
    'x': points,
    'y': team,
    'orientation': 'h',
    'marker': {
        'colorscale': 'purples',
        'color': points,
        'colorbar': {'title': 'Value'},

    }
}

premLayout = {
    'title': 'Premier League 20/21 Table',
    'xaxis': {
        'tickmode': 'linear',
    },
    'yaxis': {
        'title': '',
    },
    'template': 'plotly_dark'

}


# prem table last 10 ish
premTableLast10 = {
    'type': 'bar',
    'x': pointsLast10,
    'y': teamLast10,
    'orientation': 'h',
    'marker': {
        'colorscale': 'purples',
        'color': pointsLast10,
        'colorbar': {'title': 'Value'},

    }
}

premLayoutLast10 = {
    'title': 'Premier League 20/21 Table Last 10 Games',
    'xaxis': {
        'tickmode': 'linear',
    },
    'yaxis': {
        'title': '',
    },
    'template': 'plotly_dark'

}


# i dont know

# ratio of meaningful goals/game
scatterData1 = [{
    'type': 'scatter',
    'x': players,
    'y': meanGA,
    # 'text': players,
    'mode': 'markers',
    # 'size': 10,
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
    }]
scatLayout1 = {
    'title': 'Meaning in the Prem 20/21',
    'xaxis': {
        'title': 'Most Meaningful Players',
    },
    'yaxis': {
        'title': 'Meaningful Goals/Assists',
    },
    'template': 'plotly_dark'

}


offline.plot({'data': scatterData, 'layout': scatLayout}, filename='meaningInThePrem.html')
offline.plot({'data': goalBars, 'layout': gaBarLayout}, filename='goalsANDassistsPremBar.html')
offline.plot({'data': goalScatter, 'layout': gaScatLayout}, filename='goalsANDassistsPremScat.html')
offline.plot({'data': barData, 'layout': barLayout}, filename='meaningInThePrem1.html')
offline.plot({'data': premTable, 'layout': premLayout}, filename='premTable.html')
offline.plot({'data': ptDiffScat, 'layout': ptDiffLayout}, filename='ptDiff.html')
offline.plot({'data': ptContScat, 'layout': ptContLayout}, filename='ptCont.html')
offline.plot({'data': premTableLast10, 'layout': premLayoutLast10}, filename='premTableLast10.html')
