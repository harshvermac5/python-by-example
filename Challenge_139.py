import sqlite3

with sqlite3.connect("Phonebook.db") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
                   id INTEGER PRIMARY KEY,
                   firstname TEXT,
                   surname TEXT,
                   phonenumber TEXT)""")

    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES(1, 'Simon', 'Howels', '01223')""")
    db.commit()

    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES(2, 'Karen', 'Phillips', '01223')""")
    db.commit()

    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES(3, 'Darren', 'Smith', '01223')""")
    db.commit()

    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES(4, 'Anne', 'Jones', '01223')""")
    db.commit()

    cursor.execute("""INSERT INTO Names(
                   id, firstname, surname, phonenumber)
                   VALUES(5, 'Mark', 'Smith', '01223')""")
    db.commit()

db.close()
