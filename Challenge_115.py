#Books suggest you to open file in append mode, but append mode doesn't allow to view contents of file.

file = open("Books.csv", "r")
x = 0
for row in file:
    display = "Row: " + str(x) + " - " + row
    print(display)
    x = x + 1