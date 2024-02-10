import sqlite3

#opens the file
file = open("Booklist.txt", "w")

#opens the database as db, and putting the cursor for editing
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()

#small function to print name from the authors table
cursor.execute("SELECT Name from Authors")
for x in cursor.fetchall():
    print(x)

#asks for input of author name, storing into selectauthor variable
print()
selectauthor = input("Enter an author's name: ")
print()

#selects the author field, where author is our predefined variable
cursor.execute("SELECT * FROM Books WHERE Author=?", [selectauthor])
for x in cursor.fetchall():
    newrecord = str(x[0]) + "-" + x[1] + "-" + x[2] + "-" + str(x[3]) + "\n"
    file.write(newrecord)

file.close()

db.close()