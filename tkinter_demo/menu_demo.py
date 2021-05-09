from tkinter import *

root = Tk()
root.title("Menu_demo")
root.geometry("400x400")


def new_command():
    pass


# Define a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Creating a menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


root.mainloop()
