# COVID 19 Data and Visualization  

![US Counties by Date](https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/AnimatedCounties.png)

+ bigqueryCounty.py - Uses SQL with Google BigQuery to obtain public data and writes to county.csv  
+ plotCounty.py - Reads the .csv file and writes figures for each day with specified start and ending dates. Makes image folder and writes to 'date'.png 
+ countyAPNG.py - Utilizes all figures and forms the animated PNG you see here. Writes to AnimatedCounties.png
--

![State by Date](https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/GA.png)

[Interactive Link](https://htmlpreview.github.io/?https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/GA.html)
+ bigqueryCounty.py - Prerequisite
+ transformToState.py - Transforms county.csv to state.csv
+ plotState.py - Plots specified state line graph, writes to 'state'.png
--

![COVID-19 in the U.S](https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/usa.png)

[Interactive Link](https://htmlpreview.github.io/?https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/usa.html)
+ bigqueryCounty.py - Prerequisite
+ transformToUS.py - Transforms state.csv to usa.csv
+ plotCountry.py - Writes to usa.png

