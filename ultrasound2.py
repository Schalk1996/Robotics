import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIGL1 = 5
TRIGL2 = 38
TRIGR1 = 16
TRIGR2 = 40

ECHOL1 = 12
ECHOL2 = 37
ECHOR1 = 10
ECHOR2 = 36

GPIO.setup(TRIGL1,GPIO.OUT)
GPIO.setup(TRIGL2,GPIO.OUT)
GPIO.setup(TRIGR1,GPIO.OUT)
GPIO.setup(TRIGR2,GPIO.OUT)

GPIO.setup(ECHOL1,GPIO.IN)
GPIO.setup(ECHOL2,GPIO.IN)
GPIO.setup(ECHOR1,GPIO.IN)
GPIO.setup(ECHOR2,GPIO.IN)
#GPIO.cleanup()

def distanceL1():
	GPIO.output(TRIGL1, True)
	time.sleep(0.00001)
	GPIO.output(TRIGL1, False)
	
	startL1 = time.time()
	stopL1 = time.time()

	while GPIO.input(ECHOL1) == 0:
		startL1 = time.time()

	while GPIO.input(ECHOL1) == 1:
		stopL1 = time.time()

	distanceL1 = (stopL1 - startL1) * 17000
	return distanceL1

def distanceL2():
	GPIO.output(TRIGL2, True)
	time.sleep(0.00001)
	GPIO.output(TRIGL2, False)
	
	startL2 = time.time()
	stopL2 = time.time()

	while GPIO.input(ECHOL2) == 0:
		startL2 = time.time()

	while GPIO.input(ECHOL2) == 1:
		stopL2 = time.time()

	distanceL2 = (stopL2 - startL2) * 17000
	return distanceL2

def distanceR1():
	GPIO.output(TRIGR1, True)
	time.sleep(0.00001)
	GPIO.output(TRIGR1, False)
	
	startR1 = time.time()
	stopR1 = time.time()

	while GPIO.input(ECHOR1) == 0:
		startR1 = time.time()

	while GPIO.input(ECHOR1) == 1:
		stopR1 = time.time()

	distanceR1 = (stopR1 - startR1) * 17000
	return distanceR1
    
def distanceR2():
	GPIO.output(TRIGR2, True)
	time.sleep(0.00001)
	GPIO.output(TRIGR2, False)
	
	startR2 = time.time()
	stopR2 = time.time()

	while GPIO.input(ECHOR2) == 0:
		startR2 = time.time()

	while GPIO.input(ECHOR2) == 1:
		stopR2 = time.time()

	distanceR2 = (stopR2 - startR2) * 17000
	return distanceR2

if __name__ == '__main__':
	try:
		while True:
                        distL2 = distanceL2()
                        distR2 = distanceR2()
			distL1 = distanceL1()
			distR1 = distanceR1()
			#distR2 = distanceR2()
			
			print "R1 = %.1f cm, R2 = %.1f cm, L1 = %.1f cm, L2 = %.1f cm" % (distR1, distR2, distL1, distL2)
			time.sleep(1)

	except KeyboardInterrupt:
		print "Measurement stopped by user"
		GPIO.cleanup()

#print "sleep"

#time.sleep(0.1)

#print "starting measurement..."

#GPIO.output(TRIG,1)
#print "Triggerd"
#time.sleep(0.00001)

#GPIO.output(TRIG,0)
#print "Entering While"

#while GPIO.input(ECHO) == 0:
#	print "IN WHILE"
#start = time.time()

#while GPIO.input(ECHO) == 1:
#	print "IN WHILE 2"
#stop = time.time()

#print (stop - start) * 17000

#GPIO.cleanup()
