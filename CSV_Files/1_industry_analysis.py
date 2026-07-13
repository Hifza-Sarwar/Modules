import csv
# 1.filter the value less than 1000
file1=open("indusrty_file.csv","r")
data=csv.reader(file1)
for row in data:
        if int(row[5])<1000:
                print(row)


#2. Show only the data whose industry_code is A and E
file1=open("indusrty_file.csv","r")
data=csv.reader(file1)
for row in data:
        if "A" and "E" in row[1]:
                print(row)


#3.Show data with unit Count
file1=open("indusrty_file.csv","r")
data=csv.reader(file1)
for row in data:
        if row[6]=="COUNT":
                print(row)
       

        
file1.close()

