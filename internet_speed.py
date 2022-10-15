from tkinter import *
import speedtest

def speedcheck():
    sp= speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    num1.config(text = down)
    num2.config(text = up)

tk = Tk()

tk.configure(bg='light grey')
tk.geometry('450x450')
lab = Label(tk,text = "My Internet speedtest",font= ('Arial bold','20'),bg = 'light grey')
lab.place(anchor = NW)

lab1 = Label(tk,text = "Download speed :",font= ('Arial bold','20'),bg = 'light grey')
lab1.place(x = 20,y =60,anchor = NW)
num1 = Label(tk,text = "calculating..",font= ('Arial bold','15'),bg = 'light grey')
num1.place(x = 270,y =60,anchor = NW)

lab3 = Label(tk,text = "Upload speed :",font= ('Arial bold','20'),bg = 'light grey')
lab3.place(x = 20,y =140,anchor = NW)
num2 = Label(tk,text = "calculating..",font= ('Arial bold','15'),bg = 'light grey')
num2.place(x = 230,y =140,anchor = NW)

lab4 = Button(tk, text="Test",font= ('Arial bold','20'),relief=RAISED,bg='blue',command = speedcheck)
lab4.place(x = 40,y = 210,height = 100,width = 200)
mainloop()