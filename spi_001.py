from machine import Pin, SPI

oe = Pin(33, )
spi = SPI(2, baudrate=80000000, polarity=1,phase=0,bits=8, firstbit=0, sck=Pin(18),mosi=Pin(23), miso=Pin(19))
spi.init(baudrate=8000000)
spi.write(b'65')
