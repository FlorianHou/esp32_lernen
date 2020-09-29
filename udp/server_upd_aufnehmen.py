from math import pi
import sys
import time
from socket import *

#Socket
HOST = ''
PORT = 4001
BUFSIZ = 128
ADDR = (HOST, PORT)

udpSerrverSocket = socket(AF_INET, SOCK_DGRAM) 
udpSerrverSocket.bind(ADDR) 

time.sleep(0.5)

while True: 
    print('Warten...')
    data, addr = udpSerrverSocket.recvfrom(BUFSIZ)  
    print('Address:', addr)

    res = bytes(data.strip()).decode("utf-8")[1:-1]
    res = map(float, res.split(","))
    res = map(lambda x: round(x,4), res)
    xl, xr, yl, yr, pl, pr = res
    pl = bool(pl)
    pr = bool(pr)
    print(xl, xr, yl, yr, pl, pr)