from time import strftime
from tkinter import *
from tkinter.ttk import Label

def timer():
    string = strftime('%H:%M:%S %p') 
    lab.config(text=string)
    lab.after(1000, timer)

cl = Tk()
cl.title("CLOCK")
cl.configure(bg='light pink')
cl.geometry('400x100')

lab = Label(cl,font = ('calibri', 50, 'bold'),background='pink',foreground= 'red')
lab.pack(anchor=CENTER)
timer()

mainloop()
