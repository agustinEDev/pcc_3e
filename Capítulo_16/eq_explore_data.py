from pathlib import Path
import json

import plotly.express as px

#Lee los datos como una cadena y lo convierte en un objeto Python.
path = Path('eq_data/last_30_days.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

#Analiza todos los terremotos del conjunto de datos.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
#print(px.colors.named_colorscales()) #Muestra los colores disponibles

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    title = eq_dict['properties']['title']
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(title)

title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat = lats, lon = lons, size = mags, title = title,
                     color = mags,
                     color_continuous_scale = 'Viridis',
                     labels = {'color':'Magnitude'},
                     projection = 'natural earth',
                     hover_name = eq_titles,
                     )
fig.show()

#Crea una versión más legible del archivo de datos.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)