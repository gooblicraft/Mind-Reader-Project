from tkinter import *
from tkinter import ttk
import time, subprocess

#Mind reader program by Ed and Jayvee

#Methods
def open_progress_window(): #Progress Window
    mainWindow.withdraw()
    loadingWindow = Toplevel()
    loadingWindow.geometry('300x150')
    loadingWindow.title('Guessing')
    loadingWindow.resizable(False,False)    #Not resizable

    icon = PhotoImage(file="Beta\\media_files\\Question_mark.png") 
    loadingWindow.iconphoto(True, icon)
        
    def stopLoad():
        loading.stop()
        loading.forget()
        
    def inGuess():
        loadLabel.config(text=f"You are guessing number: {eval(entry1.get())}")

    def change_1():
        loadLabel.config(text="Testing all posible answers..")
        loadingWindow.after(1470, inGuess)

    def change_2():
        loadLabel.config(text="Scanning your brain...")
        loadingWindow.after(1470, change_1)
        
    def change_3():
        loadLabel.config(text="Finding your loaction...")
        loadingWindow.after(1469, change_2)
        
    loadLabel = Label(loadingWindow, text="Reading the Users Mind...", )
    loadLabel.pack(pady=15)
    loadLabel.after(1469, change_3 )
    
    loading = ttk.Progressbar(loadingWindow,mode="determinate", length=200)
    loading.pack(pady=3)
    loading.start()
        
    loadingWindow.after(5878, stopLoad)
    loadingWindow.mainloop()
    
#Main Window
mainWindow = Tk()
mainWindow.geometry('300x150')
mainWindow.title('Mind Reader')
mainWindow.resizable(FALSE, FALSE)  #Static yung window

#Widgets
label1 = Label(mainWindow, text='Think of a number between 1 and 10:', font=("Arial", 12))
label1.pack(pady=10)

entry1 = Entry(mainWindow, width=20)    #Wala pang command or method for getting the user input
entry1.pack(pady=10)
entry1.insert(5, "")

button1 = Button(mainWindow, text='Check my Guess', command=open_progress_window)    #nauuna yung progress window kesa sa main window
button1.pack(pady=10)

mainWindow.mainloop()

#Almost alguds na
