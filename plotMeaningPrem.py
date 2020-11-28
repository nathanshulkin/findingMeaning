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
ptDiff = []

# get the data
for i in range(len(pm.table)):
    meanScore.append(pm.daPlayers[i].getMeanScore())
    meanPoints.append(pm.daPlayers[i].getMeanPoints())
    meanApp.append(pm.daPlayers[i].getMeanApp())
    meanGA.append(pm.daPlayers[i].getMeanGA())
    totGA.append(pm.daPlayers[i].getGA())
    ptDiff.append(pm.daPlayers[i].getPointDiff())
    try:
        meaningfulGApGame.append(pm.daPlayers[i].getMeanGA()/pm.daPlayers[i].getMeanApp())
    except ZeroDivisionError:
        meaningfulGApGame.append(0)
    players.append(pm.daPlayers[i].getName())

    team.append(pm.table[i][0])
    points.append(pm.table[i][1][0])
    teamPlayed.append(pm.table[i][1][1])

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

# scatter plot, color gradient
scatterData = [{
    'type': 'scatter',
    'x': totGA,
    'y': meanGA,
    'text': players,
    'mode': 'markers+text',
    'hoverinfo': 'text+x+y',
    'textposition': 'top center',
    # 'size': 10,
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
    }]


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

# unzip dictionary into two tuples
# thisList = goals.items()
# scorers, goalNum = zip(*thisList)

# goals + assists
# bar
goalBars = [{
    'type': 'bar',
    'x': players,
    'y': goals,
    'name': 'goals',
    'width': 0.5,
    'marker_color': 'rgb(26, 118, 255)'
    },

    {
    'type': 'bar',
    'x': players,
    'y': assists,
    'name': 'assists',
    'width': 0.5,
    'marker_color': 'rgb(255, 118, 26)'
    }]

# scatter
goalScatter = [{
    'type': 'scatter',
    'x': goals,
    'y': assists,
    'text': players,
    'mode': 'markers+text',
    'hoverinfo': 'text+x+y',
    'textposition': 'top center',
    # 'size': '10',
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
}]

barData = [{
    'type': 'bar',
    'x': players,
    'y': meanGA,
    'name': 'meaningful goals/assists',
    'width': 0.5,
    'marker_color': 'rgb(26, 118, 255)'
    },

    {
    'type': 'bar',
    'x': players,
    'y': meanApp,
    'name': 'meaningful appearances',
    'width': 0.5,
    'marker_color': 'rgb(255, 118, 26)'
    }]

# scatter
ptDiffScat = [{
    'type': 'scatter',
    'x': players,
    'y': ptDiff,
    'text': ptDiff,
    'mode': 'markers+text',
    'hoverinfo': 'text+x',
    'textposition': 'top center',
    # 'size': '10',
    'marker': {
        'color': 'gold',
        'symbol': 'circle-open-dot'
        }
}]

points.reverse()
team.reverse()

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

# layout as dictionary/json for graph object
scatLayout = {
    'title': 'Meaning in the Prem 20/21',
    'xaxis': {
        'title': 'Total Goals/Assists',
        'range': [0, 18]
    },
    'yaxis': {
        'title': 'Meaningful Goals/Assists',
        'range': [0, 16]
    },
    'template': 'plotly_dark'

}

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

gaBarLayout = {
    'title': 'Goals and Assists in the Premier League 20/21',
    'xaxis': {
        'title': '',
        'tickmode': 'linear',
    },
    'yaxis': {
        'tickmode': 'linear',
    },
    'barmode': 'stack',
    'template': 'plotly_dark'

}

gaScatLayout = {
    'title': 'Goals and Assists in the Prem 20/21',
    'xaxis': {
        'title': 'Goals',
        'tickmode': 'linear',
        'range': [0, 12]
    },
    'yaxis': {
        'title': 'Assists',
        'tickmode': 'linear',
        'range': [0, 10]
    },
    'template': 'plotly_dark'

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

offline.plot({'data': scatterData, 'layout': scatLayout}, filename='meaningInThePrem.html')
offline.plot({'data': goalBars, 'layout': gaBarLayout}, filename='goalsANDassistsPremBar.html')
offline.plot({'data': goalScatter, 'layout': gaScatLayout}, filename='goalsANDassistsPremScat.html')
offline.plot({'data': barData, 'layout': barLayout}, filename='meaningInThePrem1.html')
offline.plot({'data': premTable, 'layout': premLayout}, filename='premTable.html')
offline.plot({'data': ptDiffScat, 'layout': ptDiffLayout}, filename='ptDiff.html')
