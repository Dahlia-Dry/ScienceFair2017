#Author Dahlia Dry
#Version 1.4
#Last Modified 11/8/16
#This program collects data from the sensors and writes it to a csv file.
import Adafruit_ADS1x15
import datetime
import Adafruit_BMP.BMP085  #for an older sensor, but can still control the BMP180
adc = Adafruit_ADS1x15.ADS1115()
bmp = Adafruit_BMP.BMP085(busnum=2) #bus 1 is already occupied by 
GAIN = 1                            #wind vane readings
filename ="november_15.txt"
target = open(filename, 'w')
a=  datetime.datetime.now()
time = str(a)
while time != "11/27/16 9:00:00":
	total_direction = 0
	total_temp = 0
	a = datetime.datetime.now()
	for i in range(1,20):  #take average ADC value so you don't get outlier signals
		direction = adc.read_adc(0, gain=GAIN) 
		total_direction = total_direction + direction
		temp = bmp.readTemperature()
		total_temp = total_temp + temp
	avg_direction = total / 20
	avg_temp = total / 20
	time =str(a)
	wind_direction = str(avg_direction)
	temperature = str(avg_temp)
	target.write(time)
	target.write(",")
	target.write(wind_direction)
	target.write(",")
	target.write(temperature)
	target.write("\n")
	time.sleep(60)

