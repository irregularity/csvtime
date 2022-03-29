import csv
import pandas as pd


csvfile = open('input.csv', newline='')
data = csv.reader(csvfile)
# datalist = list(csv.reader(csvfile))


# for line in data:
#     output = ""
#     for item in line:
#         output = output + item + ", "
#     print(output)

for line in data:
    print(line[2])

