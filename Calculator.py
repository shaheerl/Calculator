from tkinter import *   

root = Tk()
root.title("Shaheer's Calculator")
# creating a label widget
myLabel1 = Label(root, text="Hellow World!")
myLabel2 = Label(root, text="Sheri!")
# shoving it onto the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)

e = Entry(root)
e.pack()

def myClick():
    myLabel3 = Label(root, text=e.get())
    myLabel3.pack()

myButton = Button(root, text="Enter your Name!", command=myClick)
myButton.pack()


root.mainloop()

