# import all Files which can be used by tkinter 
from tkinter import *

#function for correct answer
def correct():
    lb = Label(text="Right Answer !").pack()
    
#function for wrong answer    
def inc():
    lb = Label(text="Wrong Answer").pack()
    
obj = Tk()
obj.title("QUIZ")
obj.geometry("500x500")

lab1 = Label(text="Who is the Prime Minister of India ?").pack()

an1 = Button(text="Pranab Mukherjee",command = inc).pack()
an2 = Button(text="Manmohan Singh",command = inc).pack()
an3 = Button(text="Rahul Gandhi",command = inc).pack()
an4 = Button(text="Prithvi Raj Chauhan",command = inc).pack()
an5 = Button(text="Narendra Modi",command = correct).pack()

obj.mainloop()
