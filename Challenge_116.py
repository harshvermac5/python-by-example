import csv

#opening the csv file
file = list(csv.reader(open("Books.csv")))

#initialising an empty list
Booklist = []

#filling the empty list
for row in file:
    Booklist.append(row)

#initialising a counter
x = 0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x = x+1

#all changes are to be made in Booklist
#deleting the constituent of the Book list
getrid = int(input("Enter a row number to delete: "))
del Booklist[getrid]

x = 0
for row in Booklist:
    #displays the counter as index for the list, then the item itself
    display = x, Booklist[x]
    print(display)
    x = x+1
alter = int(input("Which part do you want to alter: "))

x = 0
for row in Booklist[alter]:
    #displays the counter as index for the list, then the item itself
    display = x, Booklist[alter][x]
    print(display)
    x = x+1
part = int(input("Which part do you want to change? "))
newdata = input("Enter new Data: ")
Booklist[alter][part] = newdata
print(Booklist[alter])

file = open("Books.csv", "w")
x = 0
for row in Booklist:
    newrecord = Booklist[x][0] + ", " + Booklist[x][1] + ", " + Booklist[x][2] + "\n"
    file.write(newrecord)
    x = x+1
file.close()