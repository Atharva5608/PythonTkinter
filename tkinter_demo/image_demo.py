from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image")
root.geometry("389x316")
root.iconbitmap('calculator_icon.ico')

# Add images
my_image = ImageTk.PhotoImage(Image.open('nature.jpg'), width=100, height=100)
image_label = Label(image=my_image)
image_label.grid(row=0, column=0)


root.mainloop()
