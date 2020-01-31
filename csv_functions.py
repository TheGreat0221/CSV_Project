import matplotlib.pyplot as plt 
import csv 
from datetime import datetime

def get_headers(csv_file):

    header_row = next(csv_file)

    for index,column_header in enumerate(header_row):
        if column_header == "TMAX":
            tmax = index
        if column_header == "TMIN":
            tmin = index
        if column_header == "NAME":
            title_index = index
        if column_header == "DATE":
            date_index = index
    
    return(tmax,tmin,title_index,date_index)

def get_data(csv_file,highs,lows,dates,tmax,tmin,date_index,title_index):

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

    return (highs,lows,dates,title_name)