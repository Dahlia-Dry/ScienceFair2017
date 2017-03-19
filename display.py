import RPi.GPIO as GPIO
import Adafruit_ADS1x15

GPIO.setmode(GPIO.BCM) #set GPIO library in Broadcom pin numbering mode
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW) #red light @pin 22
GPIO.setup(27, GPIO.OUT, initial = GPIO.LOW) #red light @pin 27

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
direction = adc.read_adc(0, gain = GAIN)
while True: #^C to stop infinite loop
	new_direction = adc.read_adc(0, gain = GAIN)
	if new_direction - direction > 0:
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(27, GPIO.LOW)
	elif new_direction - direction < 0:
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
	direction = new_direction
	time.sleep(1)

	