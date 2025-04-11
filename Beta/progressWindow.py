from tkinter import *
from tkinter import ttk
from main import *
import time


loadingWindow = Tk()
loadingWindow.geometry('300x150')
loadingWindow.title('Guessing')
loadingWindow.lift()
loadingWindow.resizable(False,False)    #Not resizable

icon = PhotoImage(file="Beta\\media_files\\Question_mark.png") 
loadingWindow.iconphoto(False, icon)
    
def stopLoad():
    loading.stop()
    loading.forget()
    
def inGuess():
    loadLabel.config(text=f"You are guessing number: {answer}")    #may ginawa akong experiment (dikopa sinama), simple lang pero nakaka-bano (Maganda sya sa calculator)
    loadLabel.pack(pady=10)

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

