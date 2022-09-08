#!/usr/bin/python

import time
import fourletterphat as flp

flp.set_brightness(15)

flp.print_str("SPIN")
flp.show()
time.sleep(1)	
chars = ["|/-\\", "/-\|", "-\|/", "\|/-"]
count = 0
while True:
	flp.print_str(chars[count])
	flp.show()
	time.sleep(0.5)
	count += 1
	if count > 3:
		count = 0
