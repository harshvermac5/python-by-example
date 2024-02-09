import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
                   Name TEXT PRIMARY KEY,
                   Placeofbirth TEXT)""")

    cursor.execute("""INSERT INTO Authors(
                   Name,
                   Placeofbirth)
                   VALUES("Agatha Christie", "Torquay")""")
    db.commit()

    cursor.execute("""INSERT INTO Authors(
                   Name,
                   Placeofbirth)
                   VALUES("Cecelia Ahern", "Dublin")""")
    db.commit()

    cursor.execute("""INSERT INTO Authors(
                   Name,
                   Placeofbirth)
                   VALUES("J.K. Rowling", "Bristol")""")
    db.commit()

    cursor.execute("""INSERT INTO Authors(
                   Name,
                   Placeofbirth)
                   VALUES("Oscar Wilde", "Dublin")""")
    db.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
                   ID INTEGER PRIMARY KEY,
                   Title TEXT,
                   Author TEXT,
                   Datepublished INTEGER)""")

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(1, "De Profundis", "Oscar Wilde", 1905)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(2, "Chamber of Secrets", "J.K. Rowling", 1988)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(3, "Prisoner of Azkaban", "J.K. Rowling", 1999)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(4, "Lyrebird", "Cecelia Ahern", 2017)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(5, "Murder on the Orient express", "Agatha Christie", 1934)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(6, "Perfect", "Cecelia Ahern", 2017)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(7, "The Marble Collector", "Cecelia Ahern", 2016)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(8, "The Murder of the Links", "Agatha Christie", 1923)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(9, "The Picture of Dorian Gray", "Oscar Wilde", 1890)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(10, "The Secret Adversary", "Agatha Christie", 1921)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(11, "The Seven Dials Mystery", "Agatha Christie", 1929)""")
    db.commit()

    cursor.execute("""INSERT INTO Books(ID, Title, Author, Datepublished)
                   VALUES(12, "The year I met you", "Cecelia Ahern", 2014)""")
    db.commit()

db.close()
