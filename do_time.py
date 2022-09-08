#!/usr/bin/python

import time
import fourletterphat as flp

flp.set_brightness(15)

flp.print_str("TIME")
flp.show()
time.sleep(1)	
	
while True:
	tim = time.strftime("%_I%M")
	sec = time.strftime("%S")
	flp.print_str(tim)
	amp = time.strftime("%p")
	if amp == "PM":
			flp.set_decimal(3, 1)
	else:
			flp.set_decimal(3, 0)
	if int(sec) % 2 == 0:
		  flp.set_decimal(1, 1)
	else:
		  flp.set_decimal(1, 0)
	flp.show()
	time.sleep(0.1)
