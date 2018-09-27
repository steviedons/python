import csv
import matplotlib.pyplot as plt

from datetime import datetime

def convert_to_c(temp):
    """ convert the temp in Fahrenheit to Celsius"""
    return ((temp - 32) * 5) / 9

filename = "death_valley_2014.csv"
# filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#    for index, column_header in enumerate(header_row):
#        print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(convert_to_c(high))
            lows.append(convert_to_c(low))        


fig = plt.figure(dpi=100, figsize=(12, 6))
plt.plot(dates, highs, linewidth=1, c='red', alpha=0.5)
plt.plot(dates, lows, linewidth=1, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set chart title and lebel axis
plt.title("Daily High and Low Temps in 2014", fontsize=24)
plt.xlabel("", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temps in Celsius", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()