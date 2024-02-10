import sqlite3

from tkinter import *

#defining a function that takes input from the box sname and sgrade, then puts into variable and finally executing the code using the cursor commit function
def addtolist():
    newname = sname.get()
    newgrade = sgrade.get()
    cursor.execute("""INSERT INTO Scores (name, score) VALUES(?,?)""", (newname, newgrade))
    db.commit()
    sname.delete(0,END) #clears the box
    sgrade.delete(0,END)
    sname.focus() #puts the focus back on the name box

#simple function that clears the box
def clearlist():
    sname.delete(0,END)
    sgrade.delete(0,END)
    sname.focus()

#opens the database as db variable and then puts the cursor in for entering values
with sqlite3.connect("TestScore.db") as db:
    cursor = db.cursor()

#ensuring the fields in the database
cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
               id INTEGER PRIMARY KEY,
               name TEXT,
               score INTEGER)""")

window = Tk()
window.title("TestScores")
window.geometry("450x200")

label1 = Label(text="Enter Student's name: ")
label1.place(x= 30, y=35)

sname = Entry(text="")
sname.place(x=150, y=35, width=200, height=25)
sname.focus()

label2 = Label(text="Enter student's grade: ")
label2.place(x=30, y=80)

sgrade = Entry(text="")
sgrade.place(x=150, y=80, width=200, height=25)
# sgrade.focus() #commenting out the focus, for the second time as the focus used last time is executed

addbtn = Button(text="Add", command=addtolist)
addbtn.place(x=150, y=120, width=75, height=25)

clearbtn = Button(text="Clear", command=clearlist)
clearbtn.place(x=250, y=120, width=75, height=25)

window.mainloop()
db.close()