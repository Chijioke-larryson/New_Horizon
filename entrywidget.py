from tkinter import *

window = Tk()

def submit():
    user_input = entry.get()
    print(f"You entered: {user_input}")

def delete():
    entry.delete(0, END)
    print("Deleting.....Successfully")
def backspace():
    entry.delete(len(entry.get())-1, END)
    print("Backspacing.....Successfully")

entry = Entry(window,
              font=("Arial", 24),
              fg="green",
              bg="lightgray",
              show="*"
              )
entry.pack(side=TOP, fill=X, padx=20, pady=20)

submit_button = Button(window,
                       text="Submit",
                       font=("Arial", 24),
                       fg="green",
                       bg="lightgray",
                       command= submit
                          )
submit_button.pack(side=TOP, fill=X, padx=20, pady=20)
delete_button = Button(window,
                       text="Delete",
                       font=("Arial", 24),
                       fg="green",
                       bg="lightgray",
                       command= delete
                          )
delete_button.pack(side=TOP, fill=X, padx=20, pady=20)

backspace_button = Button(window,
                       text="Backspace",
                       font=("Arial", 24),
                       fg="green",
                       bg="lightgray",
                       command= backspace
                          )
backspace_button.pack(side=TOP, fill=X, padx=20, pady=20)


window.mainloop()