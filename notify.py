import schedule, time
from winotify import Notification, audio
import winsound
import pyttsx3
engine = pyttsx3.init()

def wakeup():
    toast = Notification(app_id="Notificii",
                        title = "Wake Up!!",
                        msg = "Good Morning!",
                        duration="long",
                        icon=r"E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/GM.jpg")
    
    winsound.PlaySound("E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/GM.wav",winsound.SND_ASYNC)
            
    toast.show()
    return schedule.CancelJob

schedule.every().day.at('5:30').do(wakeup)

def work():
    toast = Notification(app_id="Notificii",
                        title = "Knock Knock! It's Study Time!",
                        msg = "Studyyyyy!!!",
                        duration="long",
                        icon=r"E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/MINI- PROJECTS/Notificii/Brain bulb.png")

    engine.say("Knock Knock! It's Study Time!")
    engine.runAndWait()

    toast.set_audio(audio.LoopingCall, loop=False)
    
    toast.add_actions(label="Click Me!", launch="https://youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2")
    toast.show()

    return schedule.CancelJob

#schedule.every(5).to(15).seconds.do(work)
schedule.every().day.at('12:27').do(work)

while 1:
    schedule.run_pending()
    #schedule.run_all(delay_seconds=10)
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