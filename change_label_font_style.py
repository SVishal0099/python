import tkinter as tk
parent = tk.Tk()
parent.title("Welcome to India")
my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 90))
my_label.grid(column=0, row=0)
parent.mainloop()