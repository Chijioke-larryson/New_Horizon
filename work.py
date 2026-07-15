from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("My First GUI")

icon = PhotoImage(file="code.png")
window.iconphoto(True, icon)
window.config(bg="lightblue")

window.mainloop()

