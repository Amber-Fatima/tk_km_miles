from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=50,pady=50)


entry = Entry(width=30)
entry.grid(row = 0, column = 1)

l1 = Label(text="Miles")
l1.grid(row=0, column=2)

l2 = Label(text="is equal to")
l2.grid(row = 1, column = 0)


l3 = Label(text="0")
l3.grid(row = 1, column = 1)


l4 = Label(text="Km")
l4.grid(row = 1, column = 2)


def action():
    a=entry.get()
    l3.config(text=f"{round(int(a)*1.60934,2)}")


button = Button(text="Calculate", command=action)
button.grid(row=2,column=1)

window.mainloop()

