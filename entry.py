from tkinter import *
# from tkinter import Tk

window = Tk()

def submit():
    input_text = entry.get()
    print(f"You entered: {input_text}")

def delete():
    entry.delete(0, END)
    print("Sending to Trash......")
def edit():
    entry.delete(len(entry.get())-1, END)
    print("Editing.....Successfully")

entry = Entry(window,
              font=("Arial", 24),
              fg="green",
              bg="lightgray",
            #   show="*"
              )
entry.pack()

submit_button = Button(window,
                       text="Submit",
                       font=("Arial", 24),
                       fg="red",
                       bg="lightgray",
                       command = submit
                          )

submit_button.pack()

delete_button = Button(window,
                       text="Delete",
                       font=("Arial", 24),
                       fg="green",
                       bg="lightgray",
                       command = delete
                          )
delete_button.pack()
edit_button = Button(window,
                       text="Edit",
                       font=("Arial", 24),
                       fg="red",
                       bg="lightgray",
                       command = edit
                          )
edit_button.pack()
window.mainloop()

