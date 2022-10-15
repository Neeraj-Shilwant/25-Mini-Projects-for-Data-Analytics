# import modules
from cgitb import text
from tkinter import *
import os


# user define function
def shutdown():
	return os.system("shutdown /s /t 1")

def restart():
	return os.system("shutdown /r /t 1")

def logout():
	return os.system("shutdown -l")


# tkinter object
master = Tk()

# background set to grey
master.configure(bg='light grey')
master.geometry('320x320')
Label(master,text = "My first gui",font= ('Arial bold','20'),bg = 'light grey').grid(row=0)
# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="Shutdown", command=shutdown).grid(row=1)
Button(master, text="Restart", command=restart).grid(row=2)
Button(master, text="Log out", command=logout).grid(row=3)

mainloop()
