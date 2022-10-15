from ast import Try
import random as r
from time import *

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error +=1
        except : error +=1
    return error
def speed(times,timee,usertest):
    time_delay = times-timee
    time_r = round(time_delay,2)
    speed = len(usertest)/time_r
    return round(abs(speed))

text = ["Neeraj is a good boy","The resposible is a good man","The child is one of the future of the country"]
text1 = r.choice(text)
print(" ******************typing speed calculator****************")
print(text1)
time1 = time()
n = input("Type the above line :")
time2 = time()
print("Speed : ",speed(time1,time2,n), " word/sec ")
print("Error : ",mistake(text1,n))