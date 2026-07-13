import csv
# 1.Display all records where country is china
file3=open("COVID-19.csv","r")
data3=csv.reader(file3)
for row in data3:
    if "China" in row[4]:
        print(row)

#2.Shows the record of year 2015
file3=open("COVID-19.csv","r")
data3=csv.reader(file3)
next(data3)
for row in data3:
    if int(row[1])==2015:
        print(row)

#3.Shows the record of weekday only monday and tuesday
file3=open("COVID-19.csv","r")
data3=csv.reader(file3)
next(data3)
for row in data3:
    if "Monday" and "Tuesday" in row[3]:
        print(row)


#4.Shows the record where country name start with letter U
file3=open("COVID-19.csv","r")
data3=csv.reader(file3)
next(data3)
for row in data3:
    if row[4].startswith("U"):
        print(row)


