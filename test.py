#!/usr/bin/python

import time
import fourletterphat as flp

flp.set_brightness(15)

while True:
    tim = time.strftime("%H%M")
    sec = time.strftime("%S")
    flp.print_str(tim)
    amp = time.strftime("%p")
    if int(sec) % 2 == 0:
        flp.set_decimal(1, 1)
    else:
        flp.set_decimal(1, 0)
    flp.show()
    time.sleep(0.1)
