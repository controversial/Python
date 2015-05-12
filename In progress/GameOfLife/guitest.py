from Tkinter import *
import os
from PIL import Image, ImageTk

tk = Tk()
value = 0
#Load images
eraser_image = Image.open("Resources/Icons/eraser-white.png")
icon_eraser = ImageTk.PhotoImage(eraser_image)
open_image = Image.open("Resources/Icons/open-white.png")
icon_open = ImageTk.PhotoImage(open_image)
pencil_image = Image.open("Resources/Icons/pencil-white.png")
icon_pencil = ImageTk.PhotoImage(pencil_image)
save_image = Image.open("Resources/Icons/save-white.png")
icon_save = ImageTk.PhotoImage(save_image)


contents = os.listdir('Saved Images')
images = []

for x in contents:
    if x.endswith('.jpg'):
        images.append(x)
images.sort()
def load(filename):
    print filename

def drawcmd():
    print 'draw'

def erasecmd():
    print 'erase'

def opencmd():
    global fileselect
    fileselect = Toplevel()

    #Create the label about openable files
    openlabel = Label(fileselect, text="Openable Patterns")
    openlabel.pack(side=TOP)

    scrollbar = Scrollbar(fileselect, )
    scrollbar.pack(side=RIGHT, fill=Y)

    global listbox
    listbox = Listbox(fileselect, height=5, yscrollcommand=scrollbar.set)
    listbox.pack(side=LEFT, fill=BOTH)

    for item in images:
        listbox.insert(END, item)
    for x in range(20):
        listbox.insert(END, str(x))

    scrollbar.config(command=listbox.yview)
def savefile():
    print entry.get()

def savecmd():
    global savedialog
    savedialog = Toplevel()
    
    savelabel = Label(savedialog, text="Save the current pattern as:")
    savelabel.grid(row=0, column=0, columnspan=2)

    global entry
    entry = Entry(savedialog, width=15)
    entry.grid(row=1, column=0, sticky=W)

    savebutton = Button(savedialog, text='Save', command=savefile)
    savebutton.grid(row=1, column=1)


#Create the frame in which the buttons are contained
frame = Frame(tk)
frame.grid(row=1, column=0)

#Create the tkinter buttons
pencilbutton = Button(tk, image=icon_pencil, width="60", height="60", command=drawcmd)
pencilbutton.grid(row=0, column=0)

eraserbutton = Button(tk, image=icon_eraser, width="60", height="60", command=erasecmd)
eraserbutton.grid(row=1, column=0)

openbutton = Button(tk, image=icon_open, width="60", height="60", command=opencmd)
openbutton.grid(row=2, column=0)

savebutton = Button(tk, image=icon_save, width="60", height="60", command=savecmd)
savebutton.grid(row=3, column=0)


while 1:
    try:
        items = map(int, listbox.curselection())
        if len(items) != 0:
            selection = items[0]
            value = listbox.get(selection)
            print value
    except KeyboardInterrupt:
        raise
    except:
        pass
    tk.update()

