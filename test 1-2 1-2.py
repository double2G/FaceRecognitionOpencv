from VideoCapture import Device
from Tkinter import *
f=Tk()
cam=Device()
def loop():
    global photo
    cam.saveSnapshot('stream.gif')
    photo=PhotoImage(file='stream.gif')
    a.configure(image=photo)
    a.after(1,loop)
 
cam.saveSnapshot('stream.gif')
photo=PhotoImage(file='stream.gif')
a=Label(image=photo)
loop()
a.pack()
f.mainloop()