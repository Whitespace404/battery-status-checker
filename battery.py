import psutil
from time import sleep as wait
import winsound
run_ = True

while run_:
    battery = psutil.sensors_battery()
    percent = str(battery.percent)

    plugged = battery.power_plugged

    if int(percent) > 95 and plugged:
        print("stop charging")

        for i in range(1, 10):
            winsound.PlaySound("?", winsound.SND_ALIAS)
        
    wait(60)
    print(percent + "%")
