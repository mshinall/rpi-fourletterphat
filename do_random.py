#!/usr/bin/python

import time
import fourletterphat as flp
import random

flp.set_brightness(15)

flp.print_str("RAND")
flp.show()
time.sleep(1)	

while True:
	flp.print_str(str(random.randint(0,9999)))
	flp.show()
	time.sleep(0.1)
