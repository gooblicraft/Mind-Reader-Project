from tkinter import *
from tkinter import ttk
import time

def progressWindow():
    laodingWindow = Tk()
    laodingWindow.geometry('300x150')
    laodingWindow.title('Guessing')

    icon = PhotoImage(file="C:\\Users\\jayve\\Documents\\Jayvee_Files\\New folder\\Mind-Reader-Project\\media_files\\Question_mark.png")
    loadingWindow.iconphoto(False, icon) 
    
    def stopLoad():
        loadingWindow.stop()
        laodingWindow.destroy()
    
    toplvllabel = Label(laodingWindow, text="Reading the Users Mind...")
    toplvllabel.pack(pady=15)
    
    loadingWindow = ttk.Progressbar(laodingWindow,mode="determinate", length=100)
    loadingWindow.pack(pady=3)
    loadingWindow.start()
    
    laodingWindow.after(5788, stopLoad)
    laodingWindow.lift()
    laodingWindow.mainloop()
