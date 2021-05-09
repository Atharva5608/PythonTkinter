from tkinter import *

root = Tk()
root.title("Foobar")
root.geometry("400x400")


def clicked():
    global my_label2
    input_e = e.get()
    my_label2 = Label(root, text="You have clicked " + input_e)
    my_label2.pack()


def hide():
    my_label2.pack_forget()


def show():
    my_label2.pack()


def destroy():
    my_label2.destroy()


my_label = Label(root, text="Hello There")
my_label.pack()

e = Entry(root)
e.pack(pady=20)

my_button = Button(root, text="Click me", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="Show", command=show)
show_button.pack(pady=20)

destroy_button = Button(root, text="Destroy", command=destroy)
destroy_button.pack(pady=20)

root.mainloop()
