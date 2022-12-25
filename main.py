# Merry Christmas 2022
# Written on my new laptop
import tkinter as tk
from PIL import ImageTk, Image


def merry_christmas():
    print("Merry Christmas Script")
    button.pack_forget()
    img = tk.Label(gui, image=merry_chrimbo, width=500, height=500)
    img.pack(side="top")
    Tk.geometry("500x530")
    Tk.configure(background="black")
    exit_xmas = tk.Button(text="Exit Christmas", background="red", foreground="white", command=lambda: Tk.destroy())
    exit_xmas.pack(side="bottom")


Tk = tk.Tk()
gui = tk.Frame()
gui.pack()
Tk.geometry("500x500")
merry_chrimbo = ImageTk.PhotoImage(Image.open("merry_christmas.jpg"))
Tk.title("Merry Christmas")
button = tk.Button(text="Merry Christmas", background="red", foreground="white", height=500, width=500,
                   command=lambda: merry_christmas())
button.pack()

Tk.mainloop()
