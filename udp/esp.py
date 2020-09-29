from machine import UART, Pin
from machine import ADC
from time import sleep_ms
from usocket import *
import network


def upd_send(data):
    print(data)
    s.sendto(data, ADD)
    return None

s = socket(AF_INET, SOCK_DGRAM)
BUFF = 1024
HOST = "192.168.1.109"
PORT = 4001
ADD = (HOST,PORT)

#Links Joystick
p_l = Pin(33, Pin.IN)
x_l = ADC(Pin(35)); x_l.atten(ADC.ATTN_11DB); x_l.width(ADC.WIDTH_12BIT)
y_l = ADC(Pin(32)); y_l.atten(ADC.ATTN_11DB); y_l.width(ADC.WIDTH_12BIT)

#Rechts Joystick
p_r = Pin(34, Pin.IN)
x_r = ADC(Pin(36)); x_r.atten(ADC.ATTN_11DB); x_r.width(ADC.WIDTH_12BIT)
y_r = ADC(Pin(39)); y_r.atten(ADC.ATTN_11DB); y_r.width(ADC.WIDTH_12BIT)
#Loop
while True:
    x_l_delta = x_l.read()/4096 - .5+0.03
    y_l_delta = y_l.read()/4096 - .5 + 0.03
    x_r_delta = x_r.read()/4096 - .5 +0.02
    y_r_delta = y_r.read()/4096 - .5 +0.025

    # if abs(y_l_delta) > 0.05:
    #     print("x_l: ", x_l_delta, "y_l: ", y_l_delta)
    # if abs(x_r_delta) > 0.05:
    #     print("x_r: ", x_r_delta, "y_r: ", y_r_delta)
    if abs(x_l_delta) < 0.05:
        x_l_delta = 0.0

    if abs(y_l_delta) < 0.05:
        y_l_delta = 0.0

    if abs(x_r_delta) < 0.05:
        x_r_delta = 0.0

    if abs(y_r_delta) < 0.05:
        y_r_delta = 0.0
    data = bytes(str((x_l_delta, x_r_delta, y_l_delta, y_r_delta, p_l.value(), p_r.value())), "utf-8")
    upd_send(data)
    sleep_ms(25)