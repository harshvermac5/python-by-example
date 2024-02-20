import sqlite3

# opening the target file
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# printing every entries from the Authors table
cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

# asking user to enter a place of birth, with empty spaces on top and bottom and placing the entered value in location variable
print()
location = input("Enter a place of birth: ")
print()

# query for fetching the database on the value of location
cursor.execute("""SELECT Books.Title, Books.Datepublished, Books.Author FROM Books, Authors WHERE Authors.Name=Books.Author AND Authors.PlaceofBirth=?""",[location])

# printing the updated value on the screen
for x in cursor.fetchall():
    print(x)

db.close()