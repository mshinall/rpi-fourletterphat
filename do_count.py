#!/usr/bin/python

import time
import fourletterphat as flp

flp.set_brightness(15)

flp.print_str("COUNT")
flp.show()
time.sleep(1)	

count = 0
top = 9999

while True:
	flp.print_str(str(count))
	flp.show()
	time.sleep(0.0)
	count += 1
	if count > top:
		count = 0
