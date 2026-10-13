# gui - graphical user interface
# thinter - thinter is python's built-in library used to create gui application
from tkinter import *
# creating a popup window
root = Tk()# creating a window
root.title("the first gui")# name of the window
root.geometry("300x200")# size of the window
root.mainloop()# keeps the winow open until user closes it
# note - root mean layout design of gui

from tkinter import *
# creating a popup window
root = Tk()# creating a window
root.title("the first gui")# name of the window
root.geometry("300x200")# size of the window
label = Label(root, text= "hello world") # creates a label on with given text
label.pack()#displays the label on window
root.mainloop()# keeps the winow open until user closes it
# note - pack() mean to displays the label on window

from tkinter import *
import os
root = Tk()
root.title("the first gui")
root.geometry("300x200")
print("current folder:", os.getcwd)#displays the current folder, getcwd - get current working directory
print("image exists:", os.path.exists("nature.png"))# checks the status if the image exists or not
image = PhotoImage(file="nature.png") # loads the image
label = Label(root, image=image) # creates a label on with given image
label.pack()#displays the label on window
root.mainloop()# keeps the winow open until user closes it
# note - pack() mean to displays the label on window

# updating thye single line user input
from tkinter import *
root = Tk()
root.title("input example")
root.geometry("300x200")
label = Label(root,text ="enter your name:")
label.pack()
entry = Entry(root)# creates the input box where user can enter text
entry.pack()# displays the text in input box
def display():
    name = entry.get()# it fetches the value from entry var
    print(name)# displays the value in terminal
button = Button(root, text="submit",command=display)# command is to fetch and display the value in terminal
button.pack()# triggers to display the data in terminal
root.mainloop()

# updating thye multiple line user input
from tkinter import *
root = Tk()
root.title("input example")
root.geometry("300x250")
label = Label(root,text ="enter your messege:")
label.pack()
textBox = Text(root, height =8, width=30)# creates multi-line text box
textBox.pack()
def display():
    data = textBox.get("1.0", END)# gets all the entered text, 1.0 -> gets the data from 1st line 0 index pos and END -> till end
    print(data)# displays the value in terminal
button = Button(root, text="submit",command=display)# command is to fetch and display the value in terminal
button.pack()# triggers to display the data in terminal
root.mainloop()

# gui with check button(can select multiple buttons)
from tkinter import *
root = Tk()
root.title("check button")
root.geometry("300x250")
label = Label(root,text="select your skills")
label.pack()
python = IntVar()# intvar by default stores (0->f,1->t)
c = IntVar()
check1 = Checkbutton(root,text="python",variable=python)
check1.pack()
check2 = Checkbutton(root,text="c",variable=c)
check2.pack()
def display():
    print("python:",python.get())
    print("c:",c.get())
button = Button(root, text="submit", command=display)
button.pack()
root.mainloop()

# gui with radio buttons(can select only one button)
from tkinter import *
root = Tk()
root.title("check button")
root.geometry("300x250")
label = Label(root,text="select your choice")
label.pack()
Choice = IntVar()
radio1 = Radiobutton(root,text="python",variable=Choice,value =1)# defining our own value for intvar
radio1.pack()
radio2 = Radiobutton(root,text="c",variable=Choice,value=2)
radio2.pack()
radio3 = Radiobutton(root,text="java",variable=Choice,value=3)
radio3.pack()
def display():
    print("selected option:",Choice.get())
button = Button(root, text="submit", command=display)
button.pack()
root.mainloop()

# message box - used to display a popup message
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("messagebox example")
root.geometry("300x200")
def display():
    messagebox.showinfo("message","hello students!")
    #displays another popup with given message
button = Button(root, text="click me",command=display)
button.pack()
root.mainloop()

# menu - creates a menu bar (file,edit...etc)
from tkinter import *
root = Tk()
root.title("menu example")
root.geometry("300x200")

menuBar = Menu(root)# creates a menubar 
filemenu = Menu(menuBar,tearoff=0)# creates the file menu, tearoff =0 make sure menus will not seperate from 'filemenu'

filemenu.add_command(
    label ="new",
    command=lambda: print("new clicked")
)
filemenu.add_command(
    label="open",
    command=lambda: print("openclicked")
)
filemenu.add_separator()# draws a line between menus in file menu

filemenu.add_command(
    label="exit",
    command=root.destroy
)
menuBar.add_cascade(# adds the horizontal line acroos the file menu inculding above creates menus
    label="file",
    menu=filemenu
)
root.config(menu=menuBar)# displays the menu bar
root.mainloop()