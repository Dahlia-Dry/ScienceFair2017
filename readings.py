import time
import Adafruit_ADS1x15
import pandas as pd
import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
a = datetime.datetime.today()
boolean = (a.hour == "18")
filename ="data.txt"
target = open(filename, 'w')
def timezone(date):
	y = date.hour
	y = y - 5
	value = "%s-%s-%s %s:%s:%s" %(date.year, date.month, date.day, y, date.minute, date.second)
	return value
while boolean == False:
	time_start = datetime.datetime.now()
	total = 0
	avg = 0
	a = datetime.datetime.today()
	b = timezone(a)
	for i in range(1,10):
		x = adc.read_adc(0, gain=GAIN)
		total = total + x
		avg = total / 10
	t =str(b)
	data = str(avg)
	target.write(t)
	target.write("\n")
	target.write(data)
	target.write("\n")
	time_end = datetime.datetime.now()
	dif = time_end - time_start
	dif_seconds = dif.seconds
	dif_seconds = dif_seconds - (dif.microseconds/1000000)
	time.sleep(60-dif_seconds)

