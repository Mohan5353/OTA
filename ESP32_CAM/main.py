import machine as mc
import camera as cam
from utime import sleep

led = mc.Pin(2, mc.Pin.OUT)
led.value(0)
try:
    cam.init(0, format=cam.JPEG)
except:
    pass
else:
    for mode in {"saturation", "contrast", "brightness"}:
        for i in {-2, -1, 0, 1, 2}:
            eval("cam.{}({})".format(mode, i))
            led.value(1)
            img = cam.capture()
            led.value(0)
            file = open("/sd/images_esp/" + mode + "(" + str(i) + ")" + ".jpeg", "wb")
            file.write(img)
            file.close()
            sleep(1.5)
