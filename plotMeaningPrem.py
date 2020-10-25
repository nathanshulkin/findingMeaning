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

for i in range(25):
    x_values.append(pm.theMeaning[i][1][2])
    y_values.append(pm.theMeaning[i][1][3])
    players.append(pm.theMeaning[i][0])


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

barData = {
    'type': 'bar',
    'x': players,
    'y': y_values,
    'width': 0.5,
    'marker_color': 'rgb(26, 118, 255)'
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

barLayout = {
    'title': 'Meaning in the Prem',
    'xaxis': {
        'title': 'Most Meaningful Players',
    },
    'yaxis': {
        'title': 'Meaningful Goals/Assists',
    },
}

offline.plot({'data': scatterData, 'layout': scatLayout}, filename='meaningInThePrem.html')
offline.plot({'data': barData, 'layout': barLayout}, filename='meaningInThePrem1.html')
