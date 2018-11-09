from gpiozero import Button

button = Button(23)

while True:
    if button.is_pressed:
        print("Button PRESSED!!!!")
    else:
        print("Button NOT pressed")
