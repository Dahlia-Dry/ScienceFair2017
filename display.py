import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import time

GPIO.setwarnings(False) #disable warning messages
GPIO.setmode(GPIO.BCM) #set GPIO library in Broadcom pin numbering mode
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW) #red light @pin 22
GPIO.setup(27, GPIO.OUT, initial = GPIO.LOW) #red light @pin 27
GPIO.setup(23, GPIO.IN) #button @pin 23, 5V logic

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
direction = adc.read_adc(0, gain = GAIN)
<<<<<<< HEAD

def display():
	while GPIO.input(23) == False:
		new_direction = adc.read_adc(0, gain = GAIN)
		if new_direction - direction > 0:
			GPIO.output(22, GPIO.HIGH)
			GPIO.output(27, GPIO.LOW)
		elif new_direction - direction < 0:
			GPIO.output(27, GPIO.HIGH)
			GPIO.output(22, GPIO.LOW)
		direction = new_direction
		time.sleep(1)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	GPIO.cleanup()

while True:
	if GPIO.input(24) == True:
		display()
		
	
	


	
=======
print direction
while True: #^C to stop infinite loop
	new_direction = adc.read_adc(0, gain = GAIN)
	print new_direction
	if new_direction - direction > 0:
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(27, GPIO.LOW)
	elif new_direction - direction < 0:
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
	direction = new_direction
	print direction
	time.sleep(1)
GPIO.cleanup()
>>>>>>> 04e8cd0420f62f4be00947b16cce151228a899dd
