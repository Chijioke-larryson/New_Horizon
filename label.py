from tkinter import *

window = Tk()

icon = PhotoImage(file="test.png")
# window.iconphoto(True,icon)


# label = Label(window, text="Hello World")
# label = Label(window, 
#               text="Hello World", 
#               font=("Arial", 24,"bold"),
#                 fg="blue", 
#                 bg="lightgray"
#                 )
label = Label(window,
              text="bro, do you even code?", 
              font=("Arial", 24,"italic"),
                fg="green", 
                bg="white",
                # relief=RAISED,
                bd=10,
                padx=20,
                pady=200,
               image=icon,
               
               
                               
            compound = 'bottom'
)
label.pack(side=TOP)
#label.place(x = 100, y = 100)

window.mainloop()