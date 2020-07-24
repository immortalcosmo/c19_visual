import pandas as pd
df = pd.read_csv('county.csv', index_col="date", usecols=['date', 'state', 'confirmed_cases', 'deaths'])
df= df.groupby(['date','state'])[['confirmed_cases', 'deaths']].agg('sum')
df.to_csv('state.csv')