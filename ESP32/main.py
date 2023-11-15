import machine as m
from time import sleep
led=m.Pin(2,m.Pin.OUT)
for i in range(50):
  led.value(not led.value())
  sleep(1)
