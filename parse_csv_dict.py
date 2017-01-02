import os 
import csv

filecsv=os.path.abspath('Users/yenkha/Repositories/Migration/asyldata.csv')

with open('asyldata.csv') as csvfile: #declaring variable csvfile 
  readCSV = csv.reader(csvfile)
  asylist = [] #reads entire content via a list

  for row in readCSV: 
    asylist.append(row)

csvfile.close()

print(asylist)




