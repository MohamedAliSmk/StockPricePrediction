import plotly.graph_objs as go
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                   'open': [100, 101, 102, 103, 104],
                   'high': [105, 106, 107, 108, 109],
                   'low': [99, 98, 97, 96, 95],
                   'close': [104, 105, 106, 107, 108]})

# Create the chart
trace = go.Candlestick(x=df['date'],
                       open=df['open'],
                       high=df['high'],
                       low=df['low'],
                       close=df['close'])
data = [trace]
layout = go.Layout(title='Candle Chart',
                   xaxis=dict(title='Date'),
                   yaxis=dict(title='Price'))
fig = go.Figure(data=data, layout=layout)

# Show the chart
fig.show()