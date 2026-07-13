import csv
file4=open("student-dataset.csv","r")
data4=csv.reader(file4)
for row in data4:
    print(row)

# 1.Shows the data for students whose name start with K
file4=open("student-dataset.csv","r")
data4=csv.reader(file4)
for row in data4:
    if row[1].startswith("K"):
        print(row)


# 2.Search data by id
id = input("Enter your id")
file4=open("student-dataset.csv","r")
data4=csv.reader(file4)
for row in data4:
    if row[0]==id:
        print(row)


# 3.Shows the english marks less than 2.5
file4=open("student-dataset.csv","r")
data4=csv.reader(file4)
next(data4)
for row in data4:
    if float(row[9])<2.5:
        print(row)

#4. Diplay the record of students with age 20
file4=open("student-dataset.csv","r")
data4=csv.reader(file4)
next(data4)
for row in data4:
    if int(row[8])==20:
        print(row)


    