import os
from tkinter import *
from tkinter import colorchooser, font, filedialog
from tkinter.filedialog import *
from tkinter.messagebox import *
import time


def change_color():

    color = colorchooser.askcolor()
    text_area.config(fg=color[1])


def change_font(*args):

    text_area.config(font=(font_type.get(),size_box.get()))


def cut():

    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get(1.0, END))
    text_area.delete(1.0,END)

def copy():

    text_area.clipboard_append(text_area.get(1.0, END))

def paste():

    text_area.event_generate("<<Paste>>")

def open_file():

    file = filedialog.askopenfile(defaultextension=".txt",filetypes=[('Text Files', '*.txt'),('All Files', '*')],title="Open File")
    b = file.read()
    text_area.delete(1.0,END)
    text_area.insert(1.0,b)
    window.title(str(file.name))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0,END)

def save_file():
    file2 = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[('Text Files', '*.txt'),('All Files', '*')],title="Save File")
    file2.write(text_area.get(1.0,END))

def click(*args):

    scrollbar.config(command=text_area.yview)








window = Tk()
window.geometry("500x500")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width/2) - int(window.winfo_screenwidth()/2)
y = int(screen_height/2) - int(window.winfo_screenheight()/2)





size_box = Spinbox(window,from_=0, to=100,command=change_font)
size_box.grid(column=0,row=2,sticky="e")


font_type = StringVar()

window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area = Text(window)
text_area.grid(column=0, row=0,padx=15,pady=15,sticky="nsew")
scrollbar = Scrollbar(text_area,command=click)
scrollbar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

font = OptionMenu(window,font_type,*font.families(),command=change_font)
font.grid(column=0,row=2)

color_button = Button(window,text="Choose color",command=change_color)
color_button.grid(column=0,row=1,sticky="n")

menu = Menu(window)
window.config(menu=menu)
fileMenu = Menu(menu,tearoff=False)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=new_file)
fileMenu.add_command(label="Open",command=open_file)
fileMenu.add_command(label="Save",command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=window.destroy)
editMenu = Menu(menu,tearoff=False)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)











window.mainloop()