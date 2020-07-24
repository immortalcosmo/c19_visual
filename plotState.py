import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('state.csv', index_col="date")
state="GA" #Select any state. Example: Georgia = GA
df = df[df.state.str.contains(state)]

fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=df.index, y=df.confirmed_cases, name='Confirmed Cases',
                         line=dict(color='firebrick', width=4)))
fig.add_trace(go.Scatter(x=df.index, y=df.deaths, name = 'Deaths',
                         line=dict(color='royalblue', width=4)))

fig.update_layout(title='COVID-19 in ' + state,
                   xaxis_title='Date',
                   yaxis_title='Population')
fig.show()
fig.write_image("images/" + state + ".png")