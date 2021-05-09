from tkinter import *


def add_num():
    Label(root, text=f"Result is {(int(num1.get()) + int(num2.get()))} ",
          font=("Times", 10)).grid(row=5, column=0)


def sub_num():
    Label(root, text=f"Result is {(int(num1.get()) - int(num2.get()))} ",
          font=("Times", 10)).grid(row=5, column=0)


def mul_num():
    Label(root, text=f"Result is {(int(num1.get()) * int(num2.get()))} ",
          font=("Times", 10)).grid(row=5, column=0)


def div_num():
    Label(root, text=f"Result is {(int(num1.get()) / int(num2.get()))} ",
          font=("Times", 10)).grid(row=5, column=0)


root = Tk()
root.title("Calculator")
root.geometry("500x500")
root.iconbitmap('calculator_icon.ico')

main_label = Label(root, text="Calculator", font=("Times", 50))
main_label.grid(row=0, column=0)

num1_label = Label(root, text="First Number", font=("Times", 10))
num1_label.grid(row=1, column=0)
num1 = Entry(root)
num1.grid(row=1, column=1)

num2_label = Label(root, text="Second Number", font=("Times", 10))
num2_label.grid(row=2, column=0)
num2 = Entry(root)
num2.grid(row=2, column=1)

add_button = Button(root, text="Addition", command=add_num)
add_button.grid(row=3, column=0)

sub_button = Button(root, text="Subtraction", command=sub_num)
sub_button.grid(row=3, column=1)

mul_button = Button(root, text="Multiplication", command=mul_num)
mul_button.grid(row=4, column=0)

div_button = Button(root, text="Division", command=div_num)
div_button.grid(row=4, column=1)

root.mainloop()
