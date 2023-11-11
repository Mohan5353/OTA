import machine
from utime import sleep
led=machine.Pin(2,machine.Pin.OUT)
for i in range(10):
    #code
    led.value(not led.value())
    sleep(0.5)
