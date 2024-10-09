from tkinter import *
import tkinter.messagebox
root = tkinter.Tk()
root.title("When you press a button the message will pop up")
root.geometry('500x300')
def onClick():
    tkinter.messagebox.showinfo("Welcome to TYBBACA Student", "Hi I'm Ramesh")
button = Button(root, text="Click Me", command=onClick, height=5, width=10)
button.pack(side='bottom')
root.mainloop()