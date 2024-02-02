import csv

#filtering books by the year
start = int(input("Enter the starting year: "))
end = int(input("Enter the ending year: "))

#opening files as list
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x+1