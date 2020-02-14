import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox
from Tkinter import *
import os


top = Tkinter.Tk()
intro = top
top.title('Anglemania:Start')

def helloCallback():
   #create child window
   whatIs = Toplevel()
   whatIs.title("What is Anglemania!")
   #display message
   Label(whatIs, text="Anglemania! is a math game about angles.").pack()
   Label(whatIs, text="It is based off of gui-app.")
   Button(whatIs, text="OK", command=whatIs.destroy).pack()
def aboutCallback():
   #create child window
   about = Toplevel()
   about.title("About Anglemania!")
   #display message
   Label(about, text="Anglemania! 0.0 (29)").pack()
   Label(about).pack()
   Label(about, text="CREDITS: (NOT AFFILIATED WITH ANY OF THESE SITES)").pack()
   Label(about).pack()
   Label(about, text="Thanks to tiny.cc/tkinterguide for providing a guide.").pack
   Label(about, text="Thanks to tiny.cc/tkintertitle (see the one by user8875910) for the title bar").pack()
   Label(about, text="Thanks also to shields.io for the README.md badges").pack()
   Label(about, text="Thanks also to pythonprogramming.net/tkinter-adding-text-images/ for a nice article (can't remember what it taught me though)").pack()
   Label(about, text="Thanks so much to the Python Software Foundation and TkInter -- without you this wouldn't exist!").pack()
   Label(about, text="Thanks to smallguysit.com/index.php/2017/03/10/tkinter-create-window/ for 'from Tkinter import *'").pack()
   Label(about, text="Thanks to tiny.cc/childwindow for the guide on child windows -- it helped with this window!").pack()
   Label(about, text="Thanks to the book Python for Kids that helped me learn Python")
   Label(about).pack()
   Label(about, text="Thanks to all!").pack()
   #quit child window and return to root window
   #the button is optional here, simply use the corner x of the child window
   Button(about, text='OK', command=about.destroy).pack()
def badaCallback():
   print("Loading..")
   top.destroy()
   os.system('python levels/.gui/.selection.py')
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   BBada.pack()
def badaCB():
   BAbt.pack()
   Button(top, text='Exit', command=top.destroy).pack()
   Button(top, command=easterEggCallback).pack()
def messageWindow():
    #create child window
    newWindow = Toplevel()
    #display message
    message = "This is the child window"
    Label(newWindow, text=message).pack()
    #quit child window and return to root window
    #the button is optional here, simply use the corner x of the child window
    Button(newWindow, text='OK', command=newWindow.destroy).pack()
def menuCB():
   notCodedCallback()
def exitCallback():
	print("Okay, bye :(")
	exit()

BWhatIs = t.Button(top, text ="What is Anglemania!", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback).pack()
BSt = t.Button(top, text ="START!", command= badaCallback)
BMenu = t.Button(top, text="Show menubar", command=menuCB).pack()
BExit = t.Button(top, text="Exit :(", command=exitCallback)

txt2 = Label(top, text="Welcome to Anglemania!")

txt2.pack()

BWhatIs.pack()
BSt.pack()

tkMB.showinfo("Willkomen!", "Welcome to Anglemania!")


top.mainloop()
