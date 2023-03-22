import schedule, time
from winotify import Notification, audio

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
schedule.every().day.at('00:43').do(work)

while 1:
    schedule.run_pending()
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