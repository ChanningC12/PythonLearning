import csv

with open('EmployeeData.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    headers=readCSV

    for row in readCSV:
        print (row[0],row[1])
