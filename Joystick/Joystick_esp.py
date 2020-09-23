from time import sleep_ms
from machine import Pin
from machine import ADC

p_l = Pin(33, Pin.IN)
x_l = ADC(Pin(32)); x_l.atten(ADC.ATTN_11DB); x_l.width(ADC.WIDTH_12BIT)
y_l = ADC(Pin(35)); y_l.atten(ADC.ATTN_11DB); y_l.width(ADC.WIDTH_12BIT)

p_r = Pin(34, Pin.IN)
x_r = ADC(Pin(39)); x_r.atten(ADC.ATTN_11DB); x_r.width(ADC.WIDTH_12BIT)
y_r = ADC(Pin(36)); y_r.atten(ADC.ATTN_11DB); y_r.width(ADC.WIDTH_12BIT)


while True:
    x_l_delta = x_l.read()/4096 - .5
    y_l_delta = y_l.read()/4096 - .5
    x_r_delta = x_r.read()/4096 - .5
    y_r_delta = y_r.read()/4096 - .5

    if abs(y_l_delta) > 0.05:
        print("x_l: ", x_l_delta, "y_l: ", y_l_delta)
    if abs(x_r_delta) > 0.05:
        print("x_r: ", x_r_delta, "y_r: ", y_r_delta)
    sleep_ms(10)
