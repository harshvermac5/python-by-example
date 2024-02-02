#asking for number of enteries made
num = int(input("How many books do you want to add to the list? "))
file = open("Books.csv", "a")
for x in range(0,num):
    title = input("Enter a title: ")
    author = input("Enter author: ")
    year = input("Enter the release year: ")
    newrecord = title + "," + author + "," + year + "\n"
    file.write(str(newrecord))
file.close()

#initiating the search variable
searchauthor = input("Enter the name of the author to search: ")
file = open("Books.csv", "r")
count = 0
for row in file:
    if searchauthor in str(row):
        print(row)
        count += 1
if count == 0:
    print(f"There are no books by {searchauthor} in this list.")
file.close()