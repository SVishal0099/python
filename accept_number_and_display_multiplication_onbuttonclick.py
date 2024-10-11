from tkinter import *
def show_table():
    num = int(entry.get())
    str1=' Table of ' + str(num) + '\n-----------------\n'
    for i in range(1,11):
        str1 = str1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

    output_label.configure(text = str1, justify=LEFT)

main_window = Tk()
main_window.title("Multiplication Table")
message_label = Label(text= ' Enter a number to \n display its Table ' ,
font=( ' Verdana ' , 12))
output_label = Label(font=( ' Verdana ' , 12))
entry = Entry(font=( ' Verdana ' , 12), width=6)
calc_button = Button(text= ' Show Multiplication Table ' , font=( ' Verdana ', 12),
command=show_table)
message_label.grid(row=0, column=0,padx=10, pady=10)
entry.grid(row=0, column=1,padx=10, pady=10, ipady=10)
calc_button.grid(row=0, column=2,padx=10, pady=10)
output_label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)
mainloop()