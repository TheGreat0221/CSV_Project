import matplotlib.pyplot as plt 
import csv 
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

##print(type(header_row)) --> list

for index,column_header in enumerate(header_row):
    if column_header == "TMAX":
        tmax = index
    if column_header == "TMIN":
        tmin = index
    if column_header == "NAME":
        title_index = index
    if column_header == "DATE":
        date_index = index
    if column_header == "NAME":
        title_index == index

    ##print(index,column_header) --> index number and the column header

highs = []
lows  = []
dates = []

for row in csv_file:
    try:
        high=int(row[tmax])
        low=int(row[tmin])
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        title_name = row[title_index]

    except ValueError:
        print(f"Missing data for {current_date}")
        
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


## NEED TO FIGURE OUT SUB-PLOTS



fig = plt.figure()

plt.plot(dates,highs,color='red',alpha=0.5)
plt.plot(dates,lows,color="blue",alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) ## 1 axis, 2 y axis points so it can fill between the y axis points

## dynamic title grab
plt.title(f"Daily High Temps for {title_name} 2018",fontsize=16)

## Axis Labels
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)

## Tick parks
plt.tick_params(axis='both',which="major",labelsize=12)

## Additional Formatting
fig.autofmt_xdate() ## what is on the x axis is a date, so format correctly; draws the date labels diagonally to prevent them from overlapping

plt.show()