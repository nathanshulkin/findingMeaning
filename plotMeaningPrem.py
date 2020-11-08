# Nathan Shulkin
# show some prem stuff using plotly

# pip install plotly
from plotly.graph_objs import Scatter, Bar
from plotly.subplots import make_subplots
from plotly import offline

import premMeaning as pm


# define some data
meanApp = []
meanGA = []
meanScore = []
meanPoints = []
meaningfulGApGame = []
totGA = []
players = []
team = []
points = []
teamPlayed = []

# get the data
for i in range(len(pm.table)):
    meanScore.append(pm.theMeaning[i][1][0])
    meanPoints.append(pm.theMeaning[i][1][1])
    meanApp.append(pm.theMeaning[i][1][3])
    meanGA.append(pm.theMeaning[i][1][4])
    totGA.append(pm.theMeaning[i][1][2])
    meaningfulGApGame.append(pm.theMeaning[i][1][4]/pm.theMeaning[i][1][3])
    players.append(pm.theMeaning[i][0])

    team.append(pm.table[i][0])
    points.append(pm.table[i][1][0])
    teamPlayed.append(pm.table[i][1][1])


players.reverse()
totGA.reverse()
meanGA.reverse()
meanApp.reverse()
meanScore.reverse()
meanPoints.reverse()
meaningfulGApGame.reverse()

# scatter plot, color gradient
scatterData = [{
    'type': 'scatter',
    'x': totGA,
    'y': meanGA,
    'text': players,
    'mode': 'markers',
    'hoverinfo': 'text+x+y',
    # 'textposition': 'bottom right',
    # 'size': 10,
    'marker': {
        'colorscale': 'Bluered',
        'color': meanGA,
        'colorbar': {'title': 'Value'},
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
        'colorscale': 'Bluered',
        'color': meanGA,
        'colorbar': {'title': 'Value'},
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

barTable = {
    'type': 'bar',
    'x': team,
    'y': points
}

# layout as dictionary/json for graph object
scatLayout = {
    'title': 'Meaning in the Prem',
    'xaxis': {
        'title': 'Total Goals/Assists',
    },
    'yaxis': {
        'title': 'Meaningful Goals/Assists',
    },
}

scatLayout1 = {
    'title': 'Meaning in the Prem',
    'xaxis': {
        'title': 'Most Meaningful Players',
    },
    'yaxis': {
        'title': 'Meaningful Goals/Assists',
    },
}

barLayout = {
    'title': 'Premier League 20/21 Table',
    'xaxis': {
        'title': '',
    },
    'yaxis': {
        'tickmode': 'linear',
    },
}

offline.plot({'data': scatterData, 'layout': scatLayout}, filename='meaningInThePrem.html')
offline.plot({'data': barData, 'layout': barLayout}, filename='meaningInThePrem1.html')
offline.plot({'data': barTable, 'layout': barLayout}, filename='premTable.html')
