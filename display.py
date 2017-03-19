import RPi.GPIO as GPIO
import Adafruit_ADS1x15

GPIO.setwarnings(False) #disable warning messages
GPIO.setmode(GPIO.BCM) #set GPIO library in Broadcom pin numbering mode
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW) #red light @pin 22
GPIO.setup(27, GPIO.OUT, initial = GPIO.LOW) #red light @pin 27
GPIO.setup(23, GPIO.IN) #button @pin 23, 5V logic

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
direction = adc.read_adc(0, gain = GAIN)

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
		
	
	


	