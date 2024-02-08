import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter First name: ")
    newsname = input("Enter Surname:")
    newpnum = input("Enter Phone number:")
    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES (?,?,?,?)""",(newid, newfname, newsname, newpnum))
    db.commit()

def selectname():
    selectsurname = input("Enter a Surname: ")
    cursor.execute("SELECT * FROM Names WHERE id = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)

def deletedata():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELECT FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("Phonebook.db") as db:
    cursor = db.cursor()

def main():
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
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again = "n"
        else:
            print("Enter correct value")

main()

db.close()