from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

DURATION=const(300)
BLINK=const(3)
INTENSITY=const(0x55)

pin = Pin(21, mode=Pin.OUT)
pixel = NeoPixel(pin, 1)

def blink(r=0, g=0, b=0):
    for i in range(10):
        pixel[0] = (g, r, b)
        pixel.write()
        sleep_ms(int(DURATION/2))

        pixel[0] = (0, 0, 0)
        pixel.write()
        sleep_ms(int(DURATION/2))

while True:
    blink(r=INTENSITY)
    blink(g=INTENSITY)
    blink(b=INTENSITY)

    sleep_ms(DURATION)
