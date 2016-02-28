import csv

with open('EmployeeData.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        print (row[0],row[1])
