from ardrone import libardrone
from global_vars import *
from power_to_distance import *

from time import sleep
import os


#get RSSI (received signal strength indication) for one network
def _get_sig_pwr(essid):
	global secondary_net_interface
	x=os.popen('iwlist '+secondary_net_interface+' scan | grep -B3 "ESSID:\\"'+essid+'"').read()
	y=x.index('Signal level=')
	y+=len('Signal level=')
	z=x[y:].index(' ')
	return int(x[y:y+z])

def next_to(x,y):
	if x==y+1 or x==y-1 or x==y:
		return True
	else:
		return False

def get_sig_pwr(essid):
	prec_val=0xdeadbeef
	val=0xdeadbeef+2
	while not next_to(val,prec_val):
		prec_val=val
		val=_get_sig_pwr(essid)
		sleep(.2)
	
	if val>prec_val:
		return val
	else:
		return prec_val

def get_move_timelapse(pwr):
	if pwr>=-65:
		return 1
	elif pwr>=70:
		return 2
	else:
		return 3


#Whenever the program takeover a parrot drone, it launches *pilot_routine* to fly it away.
def pilot_routine(essid):
	global fly_away_threshold
	sleep(4)	#wait for the drone to forget his old controller - 4 sec is tested 100% working
	print 'Pilot routine started	!!!	'
	drone = libardrone.ARDrone()
	drone.set_speed(0.5)
	
	
	current=get_sig_pwr(essid)
	print current

	
	while current>=fly_away_threshold:
		drone.move_forward()
		sleep(get_move_timelapse(current))	#move forward more if is more far, less if is next to
		drone.hover()
		sleep(.2)
		new=get_sig_pwr(essid)	#update new drone distance through signal power
		print new

		if new>current:
			drone.turn_left()
			sleep(2.6666)	#turn 120 grades
			drone.hover()
		current=new
	drone.hover()
	drone.halt()
