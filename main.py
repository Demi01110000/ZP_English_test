from tkinter import *
import csv

file = open("TestQs.csv", "r")
matrix = list(csv.reader(file, delimiter=","))

window=Tk()
# add widgets here

btn=Button(window, text="Start", bg='MistyRose2', font=('Roman',20), fg='black')
btn.place(x=310, y=200)

lbl=Label(window, text="Are you ready??", fg='maroon', font=("Roman", 30))
lbl.place(x=210, y=50)

window.title('Test z angličtiny')
window.geometry("700x500+300+50") #("widthxheight+XPOS+YPOS")


# printing only the questions in the list and the options
y=0
x=0
q=1 #question num
for row in matrix:
    print("Question", q)
    print(matrix[y][x])
    print(matrix[y][x+2])
    
   
    #print(matrix[y][x+1])
    #user_answer = input('type your answer here')
    #if user_answer == correct_answer:
       # print("Correct! +1 point for you")
    #else:
        #print("nope :(")
    
    y +=1
    q +=1

window.mainloop()