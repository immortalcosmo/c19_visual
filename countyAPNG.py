from apng import APNG
import pandas as pd
date_index = pd.date_range(start='3/1/2020', end='7/21/2020') 
files = []
for date in date_index:
    files.append(("images/" + date.strftime("%Y-%m-%d")+".png", 200))
print(files)
im = APNG()
for file, delay in files:
  im.append_file(file, delay=delay)
im.save("AnimatedCounties.png")
