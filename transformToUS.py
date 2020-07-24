import pandas as pd
df = pd.read_csv('county.csv', index_col="date", usecols=['date', 'confirmed_cases', 'deaths'])
df= df.groupby(['date'])[['confirmed_cases', 'deaths']].agg('sum')
df.to_csv('usa.csv')