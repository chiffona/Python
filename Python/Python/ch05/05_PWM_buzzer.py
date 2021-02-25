import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 1)

Frq = [262, 294, 330, 349, 392, 440, 493, 523]

p.start(50)

try:
	while 1:
		for fr in Frq:
			p.ChangeFrequency(fr)
			time.sleep(0.5)
except KeyboardInterrupt:
	pass
	
p.stop()
GPIO.cleanup()
