from gpiozero import LED
from signal import pause

red_led = LED(17)

red_led.blink(1,1)

pause()
