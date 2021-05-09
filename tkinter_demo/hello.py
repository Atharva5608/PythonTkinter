from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("400x400")


my_label = Label(root, text="Hello World !", fg="red", bg="black", font="Times")
my_label.pack()
my_label2 = Label(root, text="Hello Atharva !", fg="green")
my_label2.pack()


root.mainloop()
