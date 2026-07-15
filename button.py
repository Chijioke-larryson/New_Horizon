from tkinter import *


window = Tk()
count = 0
def click():
    global count
    count += 1
    print(f"You clicked a button {count} times  ")

button = Button(window,
                text="click me!!",
                command = click,
                font =("Comic Sans", 30),
                bg='black',
                fg="green",
                activebackground="black",
                activeforeground="green",
                state=ACTIVE,
                # image=PhotoImage(file="code.png"),
                compound = 'top'
                )


button.pack()


window.mainloop()

