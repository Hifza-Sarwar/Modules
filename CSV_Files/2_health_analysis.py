import csv

#1.Shows the record of male patient
file2 = open("Health_file.csv","r")
data2 = csv.reader(file2)
for row in data2:
    if "Male" in row[1]:
      print(row)


#2.Shows the record of female patient
file2 = open("Health_file.csv","r")
data2 = csv.reader(file2)
for row in data2:
    if "Female" in row[1]:
      print(row)

# 3.Shows the record with status final
file2 = open("Health_file.csv","r")
data2 = csv.reader(file2)
for row in data2:
    if "Final" in row[1]:
      print(row)


#4. Only display record of year 2002
file2 = open("Health_file.csv","r")
data2 = csv.reader(file2)
next(data2)
for row in data2:
   if int(row[0]) ==2002:
      print(row)

# Only display record of year from 2002 to 2005
file2 = open("Health_file.csv","r")
data2 = csv.reader(file2)
next(data2)
for row in data2:
   year = int(row[0])
   if 2002<= year <=2005:
      print(row)


   

   