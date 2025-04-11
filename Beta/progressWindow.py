from tkinter import *
from tkinter import ttk
import time


laodingWindow = Tk()
laodingWindow.geometry('300x150')
laodingWindow.title('Guessing')
laodingWindow.lift()

icon = PhotoImage(file="Beta\\media_files\\Question_mark.png")  #Need maayos kase dinalabas yung icon
laodingWindow.iconphoto(False, icon)
    
def stopLoad():
    loading.stop()
    laodingWindow.destroy()
    
toplvllabel = Label(laodingWindow, text="Reading the Users Mind...")
toplvllabel.pack(pady=15)
    
loading = ttk.Progressbar(laodingWindow,mode="determinate", length=100)
loading.pack(pady=3)
loading.start()
    
laodingWindow.after(5788, stopLoad)
    
laodingWindow.mainloop()

