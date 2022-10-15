from curses.ascii import isspace
from operator import contains


e = input("Enter your email :")
if (e.count('@')==1):
    if (e[-4]=='.') or (e[-3]=='.'):
        for j in e:
            k=0
            if j==j.isspace():
                k=1
            elif j in ['_','@','.']:
                continue 
            if k==1:
                print("Wrong email3")
        else:print("Right Email")
    else:print("Wrong email2")
else:print("Wrong email1")
