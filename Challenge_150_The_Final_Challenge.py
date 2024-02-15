import sqlite3
from tkinter import *

def add_artist():
    newname = artistname.get()
    newaddress = artistadd.get()
    newtown = artisttown.get()
    newcountry = artistcountry.get()
    newpostcode = artistpostcode.get()
    cursor.execute("""INSERT INTO Artists (name, address, town, country, postcode) VALUES (?,?,?,?,?)""",(newname, newaddress, newtown, newcountry, newpostcode))
    db.commit()
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artisttown.delete(0, END)
    artistcountry.delete(0, END)
    artistpostcode.delete(0, END)
    artistname.focus()

def clear_artist():
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artisttown.delete(0, END)
    artistcountry.delete(0, END)
    artistpostcode.delete(0, END)
    artistname.focus()

def add_art():
    newartname = artname.get()
    newtitle = arttitle.get()
    newmedium = medium.get()
    newprice = artprice.get()
    cursor.execute("""INSERT INTO Art (artistid, title, medium, price) VALUES (?,?,?,?)""", (newartname, newtitle, newmedium, newprice))
    db.commit()
    artname.delete(0, END)
    arttitle.delete(0, END)
    medium.set("")
    artprice.delete(0, END)
    artistname.focus()

def clear_window():
    outputwindow.delete(0, END)

def view_artists():
    cursor.execute("SELECT * FROM Artists")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + x[5] + "\n"
        outputwindow.insert(END, newrecord)

def view_art():
    cursor.execute("SELECT * FROM Art")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ",  $" + str(x[4]) + "\n"
        outputwindow.insert(END, newrecord)

def search_artist_output():
    selectedartist = searchartist.get()
    cursor.execute("SELECT name FROM Artists WHERE artistid = ?", [selectedartist])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ",  $" + str(x[4]) + "\n"
        outputwindow.insert(END, newrecord)
    searchartist.delete(0, END)
    searchartist.focus()

def search_medium_output():
    selectedmedium = medium2.get()
    cursor.execute("""SELECT Art.pieceid, Artist.name, Art.title, Art.medium, Art.price FROM Artist, Art WHERE Artist.artistid=Art.artistid AND Art.medium=?""", [selectedmedium])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ",  $" + str(x[4]) + "\n"
        outputwindow.insert(END, newrecord)
    medium2.set("")

def search_by_price():
    minprice = selectmin.get()
    maxprice = selectmax.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.price FROM Artists, Art WHERE Artist.artistid=Art.artistid AND Art.price>=? AND Art.price<=? """,[minprice, maxprice])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ",  $" + str(x[4]) + "\n"
        outputwindow.insert(END, newrecord)
    selectmin.delete(0, END)
    selectmax.delete(0, END)
    selectmin.focus()

def sold():
    file = open("SoldArt.txt", "a")
    selectedpiece = soldpiece.get()
    cursor.execute("SELECT * FROM Art WHERE pieceid=?", [selectedpiece])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + "\n"
        file.write(newrecord)
    file.close()
    cursor.execute("DELETE FROM Art WHERE pieceid=?", [selectedpiece])
    db.commit()

with sqlite3.connect("Art.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(artistid INTEGER PRIMARY KEY, name TEXT, address TEXT, town TEXT, country TEXT, postcode TEXT);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Art(pieceid INTEGER PRIMARY KEY, artistid INTEGER, title TEXT, medium TEXT, price INTEGER);""")

window = Tk()
window.title("Art")
window.geometry("1220x600")

title1 = Label(text="Enter new details: ")
title1.place(x=10, y=10, width=100, height=25)

artistnamelabel1 = Label(text="Name: " )
artistnamelabel1.place(x=30, y=40, width=80, height=25)

artistname = Entry(text="")
artistname.place(x=110, y=40, width=200, height=25)
artistname.focus()

artistaddlabel1 = Label(text= "Address: ")
artistaddlabel1.place(x=310, y=40, width=80, height=25)

artistadd = Entry(text="")
artistadd.place(x=390, y=40, width=200, height=25)

artisttownlabel1 = Label(text= "Town: ")
artisttownlabel1.place(x=590, y=40, width=80, height=25)

artisttown = Entry(text="")
artisttown.place(x=670, y=40, width=100, height=25)

artistcountrylabel1 = Label(text="Country: ")
artistcountrylabel1.place(x=770, y=40, width=80, height=25)

artistcountry = Entry(text="")
artistcountry.place(x=850, y=40, width=100, height=25)

artistpostcodelabel1 = Label(text="Postcode: ")
artistpostcodelabel1.place(x=950, y=40, width=80, height=25)

artistpostcode = Entry(text="")
artistpostcode.place(x=1030, y=40, width=100, height=25)

addbtn = Button(text="Add Artist", command=add_artist)
addbtn.place(x=110, y=80, width=130, height=25)

clearbtn = Button(text="Clear Artist", command=clear_artist)
clearbtn.place(x=250, y=80, width=130, height=25)

artnamelabel = Label(text="Artist ID: ")
artnamelabel.place(x=30, y=120, width=80, height=25)

artname = Entry(text="")
artname.place(x=110, y=120, width=50, height=25)

arttitlelabel = Label(text="Title: ")
arttitlelabel.place(x=200, y=120, width=80, height=25)

arttitle = Entry(text="")
arttitle.place(x=280, y=120, width=280, height=25)

artmediumlabel = Label(text="Medium: ")
artmediumlabel.place(x=590, y=120, width=80, height=25)

medium = StringVar(window)
artmedium = OptionMenu(window, medium, "Oil", "Watercolor", "Ink", "Acrylic")
artmedium.place(x=670, y=120, width=100, height=25)

artpricelabel = Label(text="Price: ")
artpricelabel.place(x=770, y=120, width=80, height=25)

artprice = Entry(text="")
artprice.place(x=850, y=120, width=80, height=25)

addartbtn = Button(text="Add Piece", command=add_art)
addartbtn.place(x=110, y=150, width=130, height=25)

clearartbtn = Button(text="Clear Piece")
clearartbtn.place(x=250, y=150, width=130, height=25)

outputwindow = Listbox()
outputwindow.place(x=10, y=200, width=1000, height=350)

clearoutputwindow = Button(text="Clear Output", command=clear_window)
clearoutputwindow.place(x=1020, y=200, width=155, height=25)

viewallartists = Button(text="View all Artist", command=view_artists)
viewallartists.place(x=1020, y=230, width=155, height=25)

viewallart = Button(text="View all Art", command=view_art)
viewallart.place(x=1020, y=260, width=155, height=25)

searchartist = Entry(text="")
searchartist.place(x=1020, y=300, width=50, height=25)

searchartistbtn = Button(text="Search by artist", command=search_artist_output)
searchartistbtn.place(x=1075, y=300, width=100, height=25)

medium2 = StringVar(window)

searchmedium = OptionMenu(window, medium2, "Oil", "Watercolor", "Ink", "Acrylic")
searchmedium.place(x=1020, y=330, width=100, height=25)

searchmediumbtn = Button(text="Search", command=search_medium_output)
searchmediumbtn.place(x=1125, y=330, width=50, height=25)

minlbl1= Label(text="Min: ")
minlbl1.place(x=1020, y=360, width=75, height=25)

maxlbl1= Label(text="Max: ")
maxlbl1.place(x=1100, y=360, width=75, height=25)

selectmin = Entry(text="")
selectmin.place(x=1020, y=380, width=75, height=25)

selectmax = Entry(text="")
selectmax.place(x=1100, y=380, width=75, height=25)

searchpricebtn = Button(text="Search by Price", command=search_by_price)
searchpricebtn.place(x=1020, y=410, width=155, height=25)

soldpiece = Entry(text="")
soldpiece.place(x=1020, y=450, width=50, height=25)

soldbtn = Button(text="Sold", command=sold)
soldbtn.place(x= 1075, y=450, width=100, height=25)

window.mainloop()
db.close()