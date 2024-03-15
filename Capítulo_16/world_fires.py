from pathlib import Path
import csv

import plotly.express as px

path = Path('weather_data/world_fires_1_day.csv')
contents = path.read_text()
all_fires_data = csv.reader(contents.splitlines())

header_row = next(all_fires_data)
for index, column_header in enumerate(header_row):
    print(index, column_header)

lats, lons, brightness = [], [], []
for row in all_fires_data:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brightness.append(float(row[2]))

fig = px.scatter_geo (lat = lats, 
                      lon = lons, 
                      size = brightness, 
                      color = brightness,
                      title = 'Global Fires',
                      color_continuous_scale = 'Viridis',
                      labels = {'color':'Brightness'},
                      projection = 'natural earth',
                      )

fig.show()