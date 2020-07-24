# COVID 19 Data and Visualization  

![US Counties by Date](https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/AnimatedCounties.png)

+ bigqueryCounty.py - Uses SQL with Google BigQuery to obtain public data and write to .csv.  
+ plotCounty.py - Reads the .csv file and writes figures for each day with specified start and ending dates.  
+ countyAPNG.py - Utilizes all figures and forms the animated PNG you see here.  

![State by Date](https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/GA.png)

+ transformToState.py - Transforms county.csv to state.csv
+ plotState.py - Plots specified state line graph, writes to 'state'.png

![COVID-19 in the U.S](https://raw.githubusercontent.com/immortalcosmo/c19_visual/master/usa.png)

+ transformToUS.py - Transforms state.csv to usa.csv
+ plotCountry.py - Writes to usa.png

