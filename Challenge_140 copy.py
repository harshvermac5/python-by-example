import sqlite3

def viewphonebook(cursor):
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook(cursor, db):
    newid = int(input("Enter ID: "))
    newfname = input("Enter First name: ")
    newsname = input("Enter Surname:")
    newpnum = input("Enter Phone number:")
    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES (?,?,?,?)""",(newid, newfname, newsname, newpnum))
    db.commit()

def selectname(cursor):
    selectsurname = input("Enter a Surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)

def deletedata(cursor, db):
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

def main():
    with sqlite3.connect("Phonebook.db") as db:
        cursor = db.cursor()
        again = "y"
        while again == "y":
            print()
            print("Main Menu")
            print()
            print("1. View Phonebook")
            print("2. Add to Phonebook")
            print("3. Search for Surname")
            print("4. Delete Person from Phonebook")
            print("5. Quit")
            print()
            selection = int(input("Enter your selection: "))
            print()

            if selection == 1:
                viewphonebook(cursor)
            elif selection == 2:
                addtophonebook(cursor, db)
            elif selection == 3:
                selectname(cursor)
            elif selection == 4:
                deletedata(cursor, db)
            elif selection == 5:
                again = "n"
            else:
                print("Enter correct value")

if __name__ == "__main__":
    main()
