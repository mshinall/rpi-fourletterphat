#!/usr/bin/python

import time
import fourletterphat as flp


while True:
	flp.print_str(time.strftime("%I%M"))
	amp = time.strftime("%p")
	if amp == "AM":
		flp.set_decimal(1, 0)
	else:
		flp.set_decimal(1, 1)
	flp.show()
	time.sleep(0.1)


