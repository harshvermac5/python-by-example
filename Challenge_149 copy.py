from tkinter import *

# improving the original code by removing boilerplate codes
def show_table():
    num = int(num_box.get())  # Convert input to integer directly
    num_list.delete(0, END)  # Clear previous table before displaying new one
    for i in range(1, 13):
        answer = i * num
        #correcting the sequence of multiplication table
        num_list.insert(END, f"{num} x {i} = {answer}")  # Use formatted string for clarity
    num_box.delete(0, END)
    num_box.focus()

# function to clear the numbox and listbox
def clear_list():
    num_box.delete(0, END)
    num_list.delete(0, END)
    num_box.focus()

window = Tk()
window.title("Times Table")
window.geometry("400x280")

label1 = Label(text="Enter a number: ")
label1.place(x=120, y=20, width=100, height=25)

num_box = Entry()
num_box.place(x=120, y=20, width=100, height=25)
num_box.focus()

button1 = Button(text="View Times Table", command=show_table)  # Added command to button
button1.place(x=250, y=20, width=120, height=25)

num_list = Listbox()
num_list.place(x=20, y=50, width=200, height=200)  # Adjusted placement and size

button2 = Button(text="Clear", command=clear_list)
button2.place(x=250, y=50, width=120, height=25)

window.mainloop()
