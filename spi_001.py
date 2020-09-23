from machine import Pin, SPI
from time import sleep_ms
from time import sleep_us
from esp32 import RMT


def STCP_puls():
    stcp.off()
    sleep_us(20)
    stcp.on()

def refresh():
    return r.write_pulses((1,), start=1)


spi = SPI(2, baudrate=115200, polarity=1,phase=1,bits=8, firstbit=1, sck=Pin(18),mosi=Pin(23), miso=Pin(19))
spi.init(baudrate=115200)
en = Pin(22, Pin.OUT, 0)
stcp = Pin(21, Pin.OUT, 0)
r = RMT(0, pin=Pin(17), clock_div=8)
while True:
    print("write")
    spi.write(bytes([0b10000000]))
    # STCP_puls()
    refresh()
    sleep_ms(500)
    break