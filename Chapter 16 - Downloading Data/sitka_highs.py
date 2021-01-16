# learn to work with csv files and the datetime module

import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # creating a reader object
    header_row = next(reader)  # go to the next line of the csv file, in this care the first line which contains the headers

    # print each header column with its index
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates, high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:  # you can iterate every row of the reader object, starting from where you left off (you have already red the header row
        current_date = datetime.strptime(row[2], '%Y-%m-%d')   # datetime module in use
        try:
            high = int(row[4])  # high temp is in the 5th position
            low = int(row[5])
        except ValueError:
            print(f"The data for the date {current_date} is missing!")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5, linewidth=1)
ax.plot(dates, lows, c='blue', alpha=0.5, linewidth=1)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
ax.set_title('Daily high and low Temperatures - 2018\nDeath Valley, CA', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # draw the date labels diagonally to prevent them from overlapping
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()