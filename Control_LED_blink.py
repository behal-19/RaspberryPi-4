import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin = 29
GPIO.setup(ledPin, GPIO.OUT)

for i in range(10):
    print("LED on")
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.5)
    print("LED off.")
    GPIO.output(ledPin, GPIO.LOW) 
    time.sleep(0.5)
