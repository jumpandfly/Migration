import os 
import csv

asylist = []
with open('asyldata.csv') as csvfile:
  readCSV = csv.reader(csvfile)

  for row in readCSV: 
    asylist.append(row) #reading a list into a dictionary

print(asylist)
