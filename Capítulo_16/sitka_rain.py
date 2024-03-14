from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, str in enumerate(header_row):
    print(index, str)

dates, prcp = [], []
for line in reader:
    date = datetime.strptime(line[2], '%Y-%m-%d')
    try:
        prc = float(line[5])
    except:
        print(f"No hay datos para el {date}")
    else:
        dates.append(date)
        prcp.append(prc)

#Traza las precipitaciones.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp, color = 'blue')

#Seteamos las etiquetas
ax.set_xlabel('')
ax.set_ylabel('Daily rain', fontsize = 14)
ax.set_title("Sitka Rain 2021", fontsize = 14)

plt.show()