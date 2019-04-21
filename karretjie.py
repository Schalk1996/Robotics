from gpiozero import PWMOutputDevice
from time import sleep

#/////// Define Motort drivers ///////
PWM_FORWARD_LEFT_PIN = 26
PWM_FORWARD_RIGHT_PIN = 13
PWM_REVERSE_LEFT_PIN = 19
PWM_REVERSE_RIGHT_PIN = 6

#//////// Initialise objects for H-Bridge PWM pins
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def allStop():
	forwardLeft.value = 0
	forwardRight.value = 0
	reverseLeft.value = 0
	reverseRight.value = 0

def forwardDrive():
        forwardLeft.value = 1
        forwardRight.value = 1
        reverseLeft.value = 0
        reverseRight.value = 0

def reverseDrive():
        forwardLeft.value = 0
        forwardRight.value = 0
        reverseLeft.value = 1
        reverseRight.value = 1

def forwardTurnleft():
        forwardLeft.value = 0.6
        forwardRight.value = 0.8
        reverseLeft.value = 0
        reverseRight.value = 0

def forwardTurnright():
        forwardLeft.value = 0.8
        forwardRight.value = 0.2
        reverseLeft.value = 0
        reverseRight.value = 0

def reverseTurnright():
        forwardLeft.value = 0
        forwardRight.value = 0
        reverseLeft.value = 0.8
        reverseRight.value = 0.2

def reverseTurnleft():
        forwardLeft.value = 0
        forwardRight.value = 0
        reverseLeft.value = 0.2
        reverseRight.value = 0.8

def main():
	allStop()
	forwardDrive()
	sleep(5)
	reverseDrive()
	sleep(5)
	forwardTurnleft()
	sleep(5)
	forwardTurnright()
	sleep(5)
	allStop()

if __name__ == "__main__":
	main()
