import time
from winotify import Notification, audio

toast = Notification(app_id="NeuralNine Script",
                     title = "Knock Knock! It's Study Time!",
                     msg = "Studyyyyy!!!",
                     duration="long",
                     icon=r"")

toast.add_actions(label="Click Me!", launch="https://youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2")
toast.show()