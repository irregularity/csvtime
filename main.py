import csv
from platform import release
from tkinter import Y
import pandas as pd
import datetime as dt
from datetime import timezone as tz

from pytz import UTC, utc



csvfile = open('input.csv', newline='')
outputfile = open('output.csv', mode='w', newline='')
data = csv.reader(csvfile)
output = csv.writer(outputfile )
header = next(data, None) #skip header line
if header:
    output.writerow(header)
curr_time = dt.datetime.now(tz.utc)
timezonechange = dt.timedelta(hours=12)

# print(curr_time.today())
# print(curr_time.time())
# currday = curr_time.day
# currmonth = curr_time.month
# curryear = curr_time.year

# currhour = curr_time.hour
# currminute = curr_time.minute

# print(str(currmonth) + "," + str(currday) + "," + str(curryear) + " - " + str(currhour) + ":" + str(currminute))

# for line in data:
#     output = ""
#     for item in line:
#         output = output + item + ", "
#     print(output)



def releasecheck(data, output):
    for line in data:
        # linetimestamp = line[2].split() #split each timestamp entry into date/time/meridiem/timezone
        
        # lineday = linetimestamp[0].split("/") #split the date entry into m/d/y
        # linetime = linetimestamp[1].split(":") #split time into h/m
        # midday = linetimestamp[2] #AM or PM
        
        # print(line)
        # for i in range(0, len(lineday)):
        #     lineday[i] = ''.join(filter(str.isdigit, lineday[i]))      #filter out any non-digit chars in the date entry
        # for i in range(0, len(linetime)):
        #     linetime[i] = ''.join(filter(str.isdigit, linetime[i]))
        
        linedt = dt.datetime.strptime(line[2], '%m/%d/%Y, %I:%M %p %Z').replace(tzinfo=dt.timezone.utc)
    
        # if midday == "PM" :
        #     if int(linetime[0]) + 12 == 24:
        #         linetime[0] = '0'

        #     else:
        #         linetime[0] = str(int(linetime[0]) + 12)
                
                
        # linedt = dt.datetime(int(lineday[2]), int(lineday[0]), int(lineday[1]), int(linetime[0]), int(linetime[1]), tzinfo=tz.utc)
        
        if linedt < curr_time:
            line[3] = "Y"
        else:
            line[3] = "N"
            
        output.writerow(line)
        
releasecheck(data, output)
csvfile.close()
outputfile.close()


