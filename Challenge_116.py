import csv

#importing the data into the list
file = list(csv.reader(open("Books.csv")))
Booklist = []
for row in file:
    Booklist.append(row)

#printing the list to user
for row in Booklist:
    print(row)

#asking the user which line to delete
deletewhich = int(input("Which line to delete sir? "))
deletewhich = deletewhich + 1
del Booklist[deletewhich]

print(Booklist)

#asking the user which line to alter
# alterwhich = int(input("Which line to alter sir? "))
# alterwhich = alterwhich - 1
# del Booklist[alterwhich]
