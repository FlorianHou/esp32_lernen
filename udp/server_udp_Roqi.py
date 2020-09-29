# -*- coding: utf-8 -*-
from math import pi
import sys
import time
import qi
from socket import *

#Socket
HOST = ''
PORT = 4001
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerrverSocket = socket(AF_INET, SOCK_DGRAM)
udpSerrverSocket.bind(ADDR)  # 绑定服务器地址
#Qi
session = qi.Session()
session.connect("tcp://10.0.147.226:9559")
motion_service = session.service("ALMotion")
posture_service = session.service("ALRobotPosture")
motion_service.wakeUp()
# Pose initizieren
posture_service.goToPosture("Stand", 0.5)

time.sleep(0.5)

while True:  # 服务器无线循环
    try:
        print('Warten...')
        data, addr = udpSerrverSocket.recvfrom(BUFSIZ)  # 接受客户的连接
        # udpSerrverSocket.sendto(
        #     bytes('[%s] %s' % (ctime(), data), encoding='utf-8'), addr)  # 发送UDP 数据
        print('Address:', addr)

        res = bytes(data.strip()).decode("utf-8")[1:-1]
        res = map(float, res.split(","))
        res = map(lambda x: round(x,4), res)
        xl, xr, yl, yr, pl, pr = res
        pl = bool(pl)
        pr = bool(pr)
        print(xl, xr, yl, yr, pl, pr)
        x = -xl / 0.5 * 0.08
        y = yl / 0.5 * 0.05
        theta = 25 * (pi/180) * yr/0.5
        motion_service.move(x, y, theta)
        if not (pl and pr):
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("Stop")
        udpSerrverSocket.close()  # 关闭服务器连接
        motion_service.stopMove()
        motion_service.rest()
        sys.exit()