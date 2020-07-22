import pandas as pd
from urllib.request import urlopen  # Loading GeoJSON with fips codes
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import plotly.express as px
df = pd.read_csv('county.csv', index_col="date")
date_index = pd.date_range(start='2/1/2020', end='6/30/2020') #From February to the end of June
for date in date_index:
    fig = px.choropleth(df.loc[date.strftime("%Y-%m-%d")], geojson=counties, locations='county_fips_code',
                    color='confirmed_cases_per_100000',

                    color_continuous_scale="Viridis",
                    range_color=(0, 1000), #Max color range is therefore 1% of total population
                    scope="usa",
                    labels={'confirmed_cases_per_100000': 'Cases per 100,000'}
                    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.write_image("images/" + date.strftime("%Y-%m-%d") + ".png")
    break
    #Uncomment break to generate all figures, will take a few minutes.
print("Figures written.")