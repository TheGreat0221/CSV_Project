import csv_functions as fn
import matplotlib.pyplot as plt 
import csv 
from datetime import datetime

##---------------------------------------------------------------------
## GET INFO FOR DEATH VALLEY
##---------------------------------------------------------------------
d_open_file = open("death_valley_2018_simple.csv", "r")

d_csv_file = csv.reader(d_open_file, delimiter=",")

tmax, tmin, title_index, date_index, = fn.get_headers(d_csv_file)

d_highs = []
d_lows  = []
d_dates = []

d_highs, d_lows, d_dates, d_title = fn.get_data(d_csv_file,d_highs,d_lows,d_dates,tmax,tmin,date_index,title_index)

##---------------------------------------------------------------------
## GET INFO FOR SITKA
##---------------------------------------------------------------------
s_open_file = open("sitka_weather_2018_simple.csv", "r")

s_csv_file = csv.reader(s_open_file, delimiter=",")

tmax, tmin, title_index, date_index = fn.get_headers(s_csv_file)

s_highs = []
s_lows  = []
s_dates = []

s_highs, s_lows, s_dates, s_title = fn.get_data(s_csv_file,s_highs,s_lows,s_dates,tmax,tmin,date_index,title_index)

## Create figure for subplots
fig,(ax1,ax2)= plt.subplots(2,sharex=True)
fig.suptitle(f"Temperature comparison between {s_title} and {d_title}")

## SITKA SUBPLOT

ax1.plot(s_dates,s_highs,color='red',alpha=0.5) ## data on plot
ax1.plot(s_dates,s_lows,color='blue',alpha=0.5) ## data on plot
ax1.fill_between(s_dates,s_highs,s_lows,facecolor='blue',alpha=0.1) 

ax1.set_title(s_title,fontsize=10)

## DEATH VALLEY SUBPLOT

ax2.plot(d_dates,d_highs,color='red',alpha=0.5) ## data on plot
ax2.plot(d_dates,d_lows,color='blue',alpha=0.5) ## data on plot
ax2.fill_between(d_dates,d_highs,d_lows,facecolor='blue',alpha=0.1) 

ax2.set_title(d_title,fontsize=10)

## Tick parks
plt.tick_params(axis='both',which="major",labelsize=12)

## Additional Formatting
fig.autofmt_xdate()

## Show
plt.show()