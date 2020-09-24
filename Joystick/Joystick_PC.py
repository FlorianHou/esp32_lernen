from serial import Serial
from math import pi
import sys
import time
import qi

session = qi.Session()
session.connect("tcp://127.0.0.1:3068")
motion_service = session.service("ALMotion")
posture_service = session.service("ALRobotPosture")
motion_service.wakeUp()
# Pose initizieren
posture_service.goToPosture("Stand", 0.5)

esp = Serial("COM5", 115200)
time.sleep(0.5)

while True:
    try:
        res = bytes(esp.readline().strip()).decode("utf-8")
        res = map(float, res.split(" "))
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
        motion_service.stopMove()
        motion_service.rest()
        sys.exit()


