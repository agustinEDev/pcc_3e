from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

def farenheit_to_celsius (temp):
    return (temp - 32) * 5/9

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

#Extrae las temperaturas máximas.
dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except:
        print(f"Missing data for {date}")
    else:
        high = farenheit_to_celsius(high)
        low = farenheit_to_celsius(low)

        highs.append(round(high, 2))
        lows.append(round(low, 2))
        dates.append(date)

#Traza las temperaturas máximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color='blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

#Da formato al trazado
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=18)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize = 16)
ax.tick_params (labelsize = 16)

plt.show()


