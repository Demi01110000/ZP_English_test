from tkinter import *

root = Tk()

def startClick():
    myLabel = Label(root, text= "Let's start the test!" )
    myLabel.pack()

startButton = Button(root, text ="Start", pady = 50, command =startClick)
startButton.pack()

root.mainloop()