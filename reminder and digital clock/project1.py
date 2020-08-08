import datetime
import time
from playsound import playsound
import digitalclock

def reminder():
    timebreak=0
    #count=int(input())*3600
    while True:
        now_time=datetime.datetime.strftime(datetime.datetime.now(),'%S')
        if timebreak !=now_time:
            playsound('sound1.mp3')
        timebreak=now_time
        time.sleep(3)
reminder()
