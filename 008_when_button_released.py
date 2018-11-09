from gpiozero import Button
from signal import pause

def say_hello():
    print("Well hello there!")

def say_goodbye():
    print("Later tater!")

button = Button(23)

button.when_pressed = say_hello
button_when_released = say_goodbye

pause()
