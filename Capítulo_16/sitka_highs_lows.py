from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

def farenheit_to_celsius (temp):
    return (temp - 32) * 5/9

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

#Extrae las temperaturas máximas.
dates, highs, lows = [], [], []
for row in reader:
    high = int(row[4])
    high = farenheit_to_celsius(high)
    highs.append(round(high, 2))

    low = int(row[5])
    low = farenheit_to_celsius(low)
    lows.append(low)

    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)

#Traza las temperaturas máximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color='blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

#Da formato al trazado
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=18)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize = 16)
ax.tick_params (labelsize = 16)

plt.show()


