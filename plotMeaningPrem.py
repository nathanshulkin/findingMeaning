# Nathan Shulkin
# show some prem stuff using plotly

# pip install plotly
from plotly.graph_objs import Scatter, Bar
from plotly.subplots import make_subplots
from plotly import offline

import premMeaning as pm

print(pm.theMeaning)

# define some data
x_values = []
y_values = []
players = []
meaningfulGApGame = []
team = []
points = []


for i in range(len(pm.table)):
    x_values.append(pm.theMeaning[i][1][2])
    y_values.append(pm.theMeaning[i][1][3])
    players.append(pm.theMeaning[i][0])
    meaningfulGApGame.append(pm.theMeaning[i][1][3]/pm.theMeaning[i][1][2])
    team.append(pm.table[i][0])
    points.append(pm.table[i][1][0])


players.reverse()
y_values.reverse()
x_values.reverse()

# scatter plot, color gradient
scatterData = [{
    'type': 'scatter',
    'x': x_values,
    'y': y_values,
    'text': players,
    'mode': 'markers',
    # 'size': 10,
    'marker': {
        'colorscale': 'Bluered',
        'color': y_values,
        'colorbar': {'title': 'Value'},
        }
    }]

# ratio of meaningful goals/game
scatterData1 = [{
    'type': 'scatter',
    'x': players,
    'y': y_values,
    # 'text': players,
    'mode': 'markers',
    # 'size': 10,
    'marker': {
        'colorscale': 'Bluered',
        'color': y_values,
        'colorbar': {'title': 'Value'},
        }
    }]

barData = [{
    'type': 'bar',
    'x': players,
    'y': y_values,
    'name': 'meaningful goals/assists',
    'width': 0.5,
    'marker_color': 'rgb(26, 118, 255)'
    },

    {
    'type': 'bar',
    'x': players,
    'y': x_values,
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
        'title': 'Meaningful Appearances',
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
    'title': 'Meaning in the Prem',
    'xaxis': {
        'title': 'Most Meaningful Players',
    },
    'yaxis': {

    },
}

offline.plot({'data': scatterData1, 'layout': scatLayout1}, filename='meaningInThePrem.html')
offline.plot({'data': barData, 'layout': barLayout}, filename='meaningInThePrem1.html')
# offline.plot({'data': barTable, 'layout': barLayout}, filename='premTable.html')
