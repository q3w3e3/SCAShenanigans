import RPi.GPIO as GPIO
import rsa
import time

# GPIO SETUP
triggerPin = 21

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(triggerPin, GPIO.OUT) # Trigger pin set as output

GPIO.output(triggerPin, GPIO.LOW)


#RSA Shit

(pubkey, privkey) = rsa.newkeys(128)

message = 'Test'.encode('utf8')

crypto = rsa.encrypt(message, pubkey)

print("Here we go! Press CTRL+C to exit")
try:
	while True:
		GPIO.output(triggerPin, GPIO.HIGH)
		rsa.decrypt(crypto, privkey)
		#time.sleep(0.001)
		GPIO.output(triggerPin, GPIO.LOW)
		time.sleep(0.005)
#Hand Interupt
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
