import os
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
import tkinter as tk

#New File
def newFile():
    global file
    canvas.title("Untitled - Notepad - *Akaza*")
    file = None
    TextArea.delete(1.0, END)
    
#Open File
def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt",filetypes = [("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        canvas.title(os.path.basename(file) + " - Notepad - *Akaza*")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
        

#Save File
def saveFile():
    global file
    file = asksaveasfilename(initialfile = 'akaza.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file =="":
            file = None

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

        canvas.title(os.path.basename(file) + " - Notepad - *Akaza*")


#Cut
def cut():
    TextArea.event_generate(("<<Cut>>"))

#Copy
def copy():
    TextArea.event_generate(("<<Copy>>"))

#Paste
def paste():
    TextArea.event_generate(("<<Paste>>"))

#About    
def about():
    showinfo("Notepad - *Akaza*", "<Simple GUI Notepad> - akaza-28")


#tkinter
canvas = tk.Tk()
canvas.geometry("750x600")
canvas.title("Notepad - *Akaza*")
canvas.config(bg= "white")

#Text Area
TextArea = Text(canvas,wrap=WORD,bg="white",font=("Product Sans",14))
TextArea.pack(expand =True, fill=BOTH)

MenuBar = Menu(canvas,font=("Product Sans",12))

#File Menu
FileMenu = Menu(MenuBar, tearoff=0,font=("Product Sans",11))
#To Create a New File
FileMenu.add_command(label="New File", command = newFile)
#To Open a pre-existing file
FileMenu.add_command(label="Open", command = openFile)
#To Save current file
FileMenu.add_command(label="Save", command = saveFile)
#To exit the app
FileMenu.add_command(label="Exit...", command = exit)
FileMenu.add_separator()
MenuBar.add_cascade(label ="File", menu = FileMenu)

#Edit Menu
EditMenu = Menu(MenuBar, tearoff=0,font=("Product Sans",11))

#To Cut the selected text
EditMenu.add_command(label="Cut", command= cut)
#To Copy the selected text
EditMenu.add_command(label="Copy", command= copy)
#To Paste the selected text
EditMenu.add_command(label="Paste", command= paste)
EditMenu.add_separator()

MenuBar.add_cascade(label ="Edit", menu = EditMenu)


#About Menu
About = Menu(MenuBar, tearoff=0,font=("Product Sans",11))
MenuBar.add_command(label = "About", command=about)

canvas.config(menu=MenuBar)

#ScrollBar
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command = TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

canvas.mainloop()