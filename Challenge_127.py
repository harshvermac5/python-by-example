from tkinter import *

#defining a function which takes input from entry box, 
def add_name():
    name = name_box.get()
    name_list.insert(END, name) #keyword "END" is a constant which established itself as the last of the list, quite like the append method
    name_box.delete(0, END) #here delete method takes a range of characters, which is from the first to last...which means that it clears the entry box soon the button function is triggered
    name_box.focus() #put the button in focus soon after triggering the function

def clear_list():
    name_list.delete(0, END) #again delete function clears the list box, ranging from start to end
    name_box.focus() #focuses the input box, after clearing the list box

window = Tk()
window.title("Names list")
window.geometry("400x200")

#placing the entry prompt
label1 = Label(text="Enter a name: ")
label1.place(x=20, y=20, width=100, height=25)

#placing the entry box
name_box = Entry(text=0)
name_box.place(x=120, y=20, width=100, height=25)
name_box.focus()

#putting the button, triggering the add_name function
button1 = Button(text="Add to list", command= add_name)
button1.place(x=250, y=20, width=100, height=25)

#placing the listbox, that accepts data triggered by add_name function
name_list = Listbox()
name_list.place(x=120, y=50, width=100, height=100)

#placing the clear list button
button2 = Button(text="Clear List", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

#initialising the main window
window.mainloop()