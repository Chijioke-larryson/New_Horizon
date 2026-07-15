from tkinter import *

def display():
    if (x.get()==1):
        print("You Agre 😂")
    else:
        print("You do not agree 😒")

window = Tk()

window.geometry("400x300")

x = IntVar()

check_button = Checkbutton(window,
                           text= "I agree to something",
                           font=('Arial',20),
                           variable = x,
                           onvalue=1,
                           offvalue=0,
                           fg ='green',
                           command = display)

check_button.pack()

window.mainloop()