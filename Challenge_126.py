from tkinter import *

#defining a function that adds the input data
def add_on():
    #num variable receives the data entered into enter_txt block, which then converted into integer
    num = enter_txt.get()
    num = int(num)
    #displays the input number as answer, when triggered
    answer = output_txt["text"]
    answer = int(answer)
    #does the actual sum, after the display of initial number
    total = num + answer
    #updates the output value to latest sum
    output_txt["text"] = total

#defining a function that resets the total value to zero
def reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()
    
total = 0
num = 0

window = Tk()
window.title("Adding together")
window.geometry("450x100")

#Placing entry prompt
enter_lb1 = Label(text="Enter a number: ")
enter_lb1.place(x=50, y=20, width=100, height=25)

#Placing the entry box, in which data are to be entered
enter_txt = Entry(text = 0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"] = "center"
enter_txt.focus()

#Placing a button to add, which triggers add_on command
add_btn = Button(text="Add", command=add_on)
add_btn.place(x=300, y=20, width= 100, height=25)

output_lb1 = Label(text="Answer = ")
output_lb1.place(x=50, y=50, width=100, height=25)

#placing a result box, with intital value of 0
output_txt = Message(text=0)
output_txt.place(x= 150, y=50, width=100, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

#placing a clear button, that triggers reset function
clear_btn = Button(text="Clear", command=reset)
clear_btn.place(x=300, y=50, width=50, height=25)

#initialising the loop
window.mainloop()