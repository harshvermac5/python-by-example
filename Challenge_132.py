from tkinter import *
import csv

#this code is same as the previous challenge i.e. Challenge 131 with slight modification, pointed out in the comments below

def save_list():
    file=open("ages.csv", "a")
    name=name_box.get()
    age=age_box.get()
    newrecord=name+", "+age+"\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

def read_list():
    name_list.delete(0, END)
    file= list(csv.reader(open("ages.csv")))
    tmp=[]
    for row in file:
        tmp.append(row)
    # print(tmp)                I've tried using append method, Listbox doesn't support this method
    # for i in tmp:
    #     name_list.append(i)
    x=0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END,data)
        x=x+1

window = Tk()
window.title("People List")
window.geometry("400x200") #the size of the box is increased

label1=Label(text="Enter a name: ")
label1.place(x=20, y=20, width=100, height=25)

name_box=Entry(text="")
name_box.place(x=120, y=20, width=100, height=25)
name_box["justify"]="left"
name_box.focus()

label2=Label(text="Enter their age: ")
label2.place(x=20, y=50, width=100, height=25)

age_box=Entry(text="")
age_box.place(x=120, y=50,width=100, height=25)
age_box["justify"]="left"

button1=Button(text="Add to list", command=save_list) #commands are changed from creating list to saving to list
button1.place(x=250, y=20, width=100, height=25)

button2=Button(text="Read List", command=read_list) #commands are changed to saving to list to reading from the list
button2.place(x=250, y=50, width=100, height=25)

label3=Label(text="Saved Names: ") #new label is added as title to the Listbox reperesenting all the names
label3.place(x=120, y=80, width=230, height=25)

name_list=Listbox() #new titlebox is added to display the contents in the same ui
name_list.place(x=120, y=80, width=230, height=100)

window.mainloop()