import machine
from utime import sleep
led=machine.Pin(2,machine.Pin.OUT)
uart=machine.UART(1,115200)
for i in range(10):
    led.value(not led.value())
    uart.write(f"{i}")
    sleep(1)
