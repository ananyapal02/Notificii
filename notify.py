import schedule, time
from winotify import Notification, audio

import multiprocessing
from playsound import playsound
import winsound

def wakeup():
    #print("Ananya Pal")
    toast = Notification(app_id="Notificii",
                     title = "Wake Up!!",
                     msg = "Good Morning!",
                     duration="long",
                     icon=r"E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/GM.jpg")
    
    #winsound.PlaySound("E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/GM.wav",winsound.SND_ASYNC)
    #winsound.PlaySound(None,0)
    #playsound('E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/GM.mp3')
    toast.set_audio(audio.LoopingAlarm, loop=False)
    '''
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    '''

    #toast.add_actions(label="Stop Alarm!", launch=None)
    #toast.add_actions(audio="E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/GM.mp3")
    toast.show()
    return schedule.CancelJob

schedule.every().day.at('01:43').do(wakeup)

def work():
    #print("Ananya Pal")
    toast = Notification(app_id="Notificii",
                     title = "Knock Knock! It's Study Time!",
                     msg = "Studyyyyy!!!",
                     duration="long",
                     icon=r"E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/Brain bulb.png")

    toast.add_actions(label="Click Me!", launch="https://youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2")
    toast.show()

    return schedule.CancelJob

#schedule.every(5).to(15).seconds.do(work)
schedule.every().day.at('01:44').do(work)

while 1:
    #schedule.run_pending()
    schedule.run_all(delay_seconds=10)
    time.sleep(1)



'''
import time
from winotify import Notification, audio

toast = Notification(app_id="NeuralNine Script",
                     title = "Knock Knock! It's Study Time!",
                     msg = "Studyyyyy!!!",
                     duration="long",
                     icon=r"")

toast.add_actions(label="Click Me!", launch="https://youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2")
toast.show()
'''