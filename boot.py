# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import network
from time import sleep
esp.osdebug(None)

wifi_dict = {"robo":"Robo2019!",
             "QUST":"zdkjxy2001CDTF"}
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
scan_list = wlan.scan()
wlan.active(False)
scan_name_list = list(map(lambda x : x[0].decode(), scan_list))
for i in scan_name_list:
    if i in wifi_dict:
        wlan.active(True)
        wlan.connect(i,wifi_dict[i])
        sleep(10)
        print(wlan.ifconfig())
        break
#import webrepl
#webrepl.start()

