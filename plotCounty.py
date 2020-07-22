import pandas as pd
from urllib.request import urlopen  # Loading GeoJSON with fips codes
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import plotly.express as px
df = pd.read_csv('county.csv', index_col="date", dtype ={'county_fips_code': 'str'})
date_index = pd.date_range(start='3/1/2020', end='7/21/2020') #Starting from March
for date in date_index:
    fig = px.choropleth(df.loc[date.strftime("%Y-%m-%d")], geojson=counties, locations='county_fips_code',
                    color='confirmed_cases_per_100000',

                    color_continuous_scale="YlOrRd",
                    range_color=(0, 2000), #Max color range is therefore 2% of total population
                    scope="usa",
                    labels={'confirmed_cases_per_100000': 'Cases per 100,000'},
                    )
    fig.update_layout(autosize=False,
                      title_text = "COVID 19 - U.S Counties<br><br>" + date.strftime("%b %d, %Y"))
    fig.write_image("images/" + date.strftime("%Y-%m-%d") + ".png")
    break
    #Uncomment break to generate all figures, will take a few minutes.
print("Figures written.")
