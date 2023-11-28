from tkinter import *
from random import randint
from PIL import Image, ImageTk
import pygame
global imageshown
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
    render=ImageTk.PhotoImage(Image.open(f"images/cheese{r}.png"))
    root.img=Label(root, image=render)
    root.img.image=render
    #img.place(x=10,y =10)
    root.img.pack()
    imageshown=True
    pygame.mixer.music.load(f"sounds/cheese{r}.mp3")
    pygame.mixer.music.play()
    
button=Button(root, text="We like cheese", command=show_cheese)
button.pack()
root.mainloop()
