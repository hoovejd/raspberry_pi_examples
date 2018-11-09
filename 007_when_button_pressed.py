from gpiozero import Button
from signal import pause

def say_hello():
    print("Well hello there!")

button = Button(23)

button.when_pressed = say_hello

pause()
