from tkinter import*
import time
import datetime
from playsound import playsound



def reminder():
    timebreak=0
    while True:
##        now_time=datetime.datetime.now().second
        now_time=datetime.datetime.strftime(datetime.datetime.now(),'%S')
        if timebreak !=now_time:
            playsound('sound1.mp3')
        timebreak=now_time
        time.sleep(3)
def times():
    string=time.strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000,times)
if __name__ =='__main__':
    root=Tk()
    root.title('clock')
    label=Label(root,bg='black',fg='white',font='arial 40 bold')
    label.grid(column=0,row=0)
    times()
    label1=Label(root,bg='black',fg='white',font='arial 40 bold')
    label1.grid(column=1,row=0)
    reminder()
    root.mainloop()
