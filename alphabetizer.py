"""GUI alphabetizer written in python and using Tkinter"""

from Tkinter import *

#Function to return an alphabetized list from a string with many words.
def alphabetize(string):
    list = string.split()
    lower = []
    for x in list:
        lower.append(x.lower())
    sort = sorted(lower)
    return sort


#Set up the GUI, having two boxes.
tk = Tk()
inputbox = Entry(tk, width=40)
inputbox.grid(row=0, column=0)
outputbox = Text(tk, height=5, width=40, wrap="word")
outputbox.grid(row=1, column=0)

while 1:
    outputbox.delete(1.0, END) #Clear the output
    currentlist = alphabetize(inputbox.get()) #Create a list that contains the alphabetized text
    #Add the words to the outputbox one by one
    for string in currentlist:
        outputbox.insert(END, string)
        outputbox.insert(END, ' ') # Add a space between the words

    #Put the updates to the screen.    
    tk.update()

