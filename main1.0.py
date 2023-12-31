from tkinter import *
from random import randint
from PIL import Image, ImageTk
import pygame, os, sys
global imageshown

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.mixer.init()
root=Tk()
root.title("Load Cheese")
root.geometry("40x60")
imageshown=False
def show_cheese():
    global imageshown
    r=randint(1,3)
    print(r)
    if imageshown==True:
        root.img.destroy()
    render=ImageTk.PhotoImage(Image.open(resource_path(f"images/cheese{r}.png")))
    root.img=Label(root, image=render)
    root.img.image=render
    #img.place(x=10,y =10)
    root.img.pack()
    imageshown=True
    pygame.mixer.music.load(resource_path(f"sounds/cheese{r}.mp3"))
    pygame.mixer.music.play()
    
button=Button(root, text="We like cheese", command=show_cheese)
button.pack()
root.mainloop()
