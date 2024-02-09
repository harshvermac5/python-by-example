from tkinter import *

#a function that reconfigures the background when triggered
def clicked():
    sel = selectcolor.get()
    window.configure(background = sel)

window = Tk()
window.title("background")
window.geometry("200x200")

#stringvar is bridge betweeen the interactive value
# means that it allows the updating of values as well as getting the values to be use inside of the function, clicked() in this case
selectcolor = StringVar(window)
selectcolor.set("grey")

colorlist = OptionMenu(window, selectcolor, "grey","red","blue","green","yellow")
colorlist.place(x=50, y=30)

clickme = Button(text="Click me!", command=clicked)
clickme.place(x=50, y=150, width=60, height=30)

window.mainloop()