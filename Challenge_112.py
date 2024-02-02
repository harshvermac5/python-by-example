#Enabling the user to enter data right from the terminal

file = open("Books.csv", "a")
#preparing the entries
title = input("Enter a title: ")
author = input("Enter author: ")
year = input("Enter the release year: ")
#assembling the entries
newrecord = title + "," + author + "," + year + "\n"
#writing to the file
file.write(str(newrecord))
file.close()
#reading the file, after update
file.open("Books.csv", "r")
for row in file:
    print(row)
#closing the file
file.close()