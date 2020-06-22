from Tkinter import *
import Tkinter
t = Tkinter

selection = t.Tk()
selection.title('Level Selection')

def runOne():
   execfile('.1.py')
   selection.destroy()
def runTwo():
   execfile('.2.py')
   selection.destroy()
def exitAM():
	exit()

B1 = Button(selection, text="1", command=runOne)
B2 = Button(selection, text="2", command=runTwo)
Cancel = Button(selection, text="Cancel", command=exitAM)

Label(selection, text = 'Select a Level ' ,
    font = ('Arial' , 17), fg = 'black', width = 11, height = 2).pack()

B1.pack()
B2.pack()
Cancel.pack()


selection.mainloop()
