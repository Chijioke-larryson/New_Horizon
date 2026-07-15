from tkinter import *
window = Tk()
def click():
    print("You clicked a button")
window.geometry("500x500")
icon = PhotoImage(file="test.png")
button = Button(window, 
                text="Click Me!",
                font=("Arial", 12), 
                command=click,
                background="black",
                foreground ="green",
                activebackground="black",
                activeforeground="green",
                image=icon,
                compound= 'top',
            
                # state=DISABLED)
)


button.pack()
window.mainloop()