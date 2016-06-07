from ardrone import libardrone
import time

#Whenever the program takeover a parrot drone, it launches *pilot_routine* to fly it away.
def pilot_routine():
	print 'Pilot routine started	!!!	'
	drone = libardrone.ARDrone()
	#drone.reset()
	drone.takeoff()
	time.sleep(2)
	drone.land()
	time.sleep(3)
	drone.halt()

def main():
	pilot_routine()

if __name__ == "__main__":
    main()