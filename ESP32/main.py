import machine as m
from time import timer
led=m.Pin(2,m.Pin.OUT)
t=timer.init(200,50,lambda t:led.value(not led.value()))
