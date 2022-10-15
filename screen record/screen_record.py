import cv2
import numpy as np
from win32api import GetSystemMetrics
import time
import pyautogui

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = [width,height]
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4",f,30.0,dim)
now = time.time()
duration = 10
end = now + duration
while True:
    image = pyautogui.screenshot()
    frame1 = np.array(image)
    frame= cv2.cvtColor(frame1 , cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end :
        break
output.release()
print("End")