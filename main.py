import csv
import pandas as pd
import datetime as dt
from datetime import timezone as tz
import pytz


csvfile = open('test.csv', newline='')
outputfile = open('test1.csv', mode='w', newline='')
data = csv.reader(csvfile)
output = csv.writer(outputfile)

header = next(data, None) #skip header line
header.append('EST')
header.append('Released?')
if header:
    output.writerow(header)
curr_time = dt.datetime.now(tz.utc)



def releasecheck(data, output):
    
    for line in data:
        line.append('')
        line.append('')
        linedt = dt.datetime.strptime(line[2], '%m/%d/%Y, %I:%M %p %Z').replace(tzinfo=dt.timezone.utc)
    
        
        if linedt < curr_time:
            line[4] = "Y"
        else:
            line[4] = "N"
            
        output.writerow(line)
        
        
def toEST(data, output):
    est = pytz.timezone('US/Eastern')
    fmt = '%m/%d/%Y, %I:%M %p %Z'
    
    #est = zoneinfo.ZoneInfo('localtime')
    for line in data:

        
        linedt = dt.datetime.strptime(line[2], '%m/%d/%Y, %I:%M %p %Z').replace(tzinfo=dt.timezone.utc)
        line[3] = linedt.astimezone(est).strftime(fmt)
        output.writerow(line)
    
    
        
#releasecheck(data, output)

# header = next(data, None) #skip header line
# csvfile.seek(0)
# outputfile.seek(0)
# header = next(data, None) #skip header line
# if header:
#     output.writerow(header)

releasecheck(data, output)
csvfile.close()
outputfile.close()
csvfile = open('test1.csv', newline='')
outputfile = open('test2.csv', mode='w', newline='')
data = csv.reader(csvfile)
output = csv.writer(outputfile)
header = next(data, None)
if header:
    output.writerow(header) #skip header line
toEST(data, output)




csvfile.close()

outputfile.close()


