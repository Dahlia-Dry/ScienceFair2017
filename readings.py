import time
import Adafruit_ADS1x15
import pandas as pd
import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
filename ="december_2.txt"
target = open(filename, 'w')
def timezone(date):
	day = date.day
	day = day - 1
	y = date.hour
	y = y + 7
	value = "%s-%s-%s %s:%s:%s" %(date.year, date.month, day, y, date.minute, date.second)
	return value
while True:
	total = 0
	avg = 0
	a = datetime.datetime.now()
	b = timezone(a)
	for i in range(1,20):
		x = adc.read_adc(0, gain=GAIN)
		total = total + x
		avg = total / 20
	t =str(b)
	data = str(avg)
	target.write(t)
	target.write(",")
	target.write(data)
	target.write("\n")
	time.sleep(60)

