from tkinter import *
import random

def click():
    num = random.randint(1,6)
    answer["text"] = num

window = Tk()
window.title("Roll a dice")
window.geometry("320x240")

button1 = Button(text="Roll", command=click, width=9, height=3)
# button1.place(x=30, y=30, width=50, height=25)
button1.pack()

answer = Message(text="")
# answer.place(x=40, y=70, width=30, height=25)
answer.pack()

window.mainloop()