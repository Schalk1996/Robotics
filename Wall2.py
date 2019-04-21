from gpiozero import PWMOutputDevice
from time import sleep
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Using BCM pin config
#/////// Define Motort drivers ///////
PWM_FORWARD_LEFT_PIN = 26
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_LEFT_PIN = 19
PWM_REVERSE_RIGHT_PIN = 6

#////// Define pins for ultrasound ///////
TRIG = 4
ECHO = 18

#////// Initialise Ultrasound
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#//////// Initialise objects for H-Bridge PWM pins
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

#/////// Calculating distance from wall
def distance():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	
	start = time.time()
	stop = time.time()

	while GPIO.input(ECHO) == 0: #Listen for echo
		start = time.time()

	while GPIO.input(ECHO) == 1: #Recieve echo
		stop = time.time()

	distance = (stop - start) * 17000

	return distance

def allStop():
	forwardLeft.value = 0
	forwardRight.value = 0
	reverseLeft.value = 0
	reverseRight.value = 0

def forwardDrive():
        forwardLeft.value = 0.4
        forwardRight.value = 0.4
        reverseLeft.value = 0
        reverseRight.value = 0

##def reverseDrive():
##        forwardLeft.value = 0
##        forwardRight.value = 0
##        reverseLeft.value = 1
##        reverseRight.value = 1

##def forwardTurnleft():
##        forwardLeft.value = 0.2
##        forwardRight.value = 0.8
##        reverseLeft.value = 0
##        reverseRight.value = 0
##
##def forwardTurnright():
##        forwardLeft.value = 0.8
##        forwardRight.value = 0.2
##        reverseLeft.value = 0
##        reverseRight.value = 0
##
##def reverseTurnright():
##        forwardLeft.value = 0
##        forwardRight.value = 0
##        reverseLeft.value = 0.8
##        reverseRight.value = 0.2
##
##def reverseTurnleft():
##        forwardLeft.value = 0
##        forwardRight.value = 0
##        reverseLeft.value = 0.2
##        reverseRight.value = 0.8

def left():
    forwardLeft.value = 0.1
    forwardRight.value = 0.2
    reverseLeft.value = 0
    reverseRight.value = 0

def right():
    forwardLeft.value = 0.2
    forwardRight.value = 0.1
    reverseLeft.value = 0
    reverseRight.value = 0

def drive():
    forwardLeft.value = 0.3
    forwardRight.value = 0.3
    reverseLeft.value = 0
    reverseRight.value = 0
    
    

def main():
	allStop()
	forwardDrive()
	sleep(8)
##	reverseDrive()
##	sleep(5)
##	forwardTurnleft()
##	sleep(5)
##	forwardTurnright()
##	sleep(5)
##	allStop()

if __name__ == "__main__":
	main()
