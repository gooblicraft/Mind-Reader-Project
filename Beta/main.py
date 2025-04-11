from tkinter import *
from tkinter import ttk
import time, subprocess

# import progressWindow (Next time natin to ayusin)

#Methods
def open_other_file():
    subprocess.Popen(["python", "Beta\\progressWindow.py"])
    mainWindow.destroy()
    
def inGuess():
    label1.config(text=f"You are guessing number: {entry1.get()}")    #may ginawa akong experiment (dikopa sinama), simple lang pero nakaka-bano (Maganda sya sa calculator)
    label1.pack(pady=10)

#Mind reader program by Ed and Jayvee
mainWindow = Tk()
mainWindow.geometry('300x150')
mainWindow.title('Mind Reader')
mainWindow.resizable(FALSE, FALSE)  #Static yung window

#Widgets
label1 = Label(mainWindow, text='Think of a number between 1 and 10:', font=("Arial", 12))
label1.pack(pady=10)

entry1 = Entry(mainWindow, width=20)    #Wala pang command or method for getting the user input
entry1.pack(pady=10)
entry1.insert(5, '')

button1 = Button(mainWindow, text='Check my Guess', command=open_other_file)    #nauuna yung progress window kesa sa main window
button1.pack(pady=10)

mainWindow.mainloop()

#Need nalang maayos ng progress bar at wala panung final verdict

