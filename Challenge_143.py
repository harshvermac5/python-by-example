import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

#asks for the input year
selectionyear = int(input("Enter a year: "))
print()

#opens the database to grab the sorted data based on the variable
cursor.execute("""SELECT Books.Title, Books.Datepublished, Books.Author FROM Books WHERE Datepublished>? ORDER BY Datepublished""",[selectionyear])

#prints the data
for x in cursor.fetchall():
    print(x)

db.close()