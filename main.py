import time
import os

from monitor import *
from global_vars import *

def check_if_nic_exists(nic_id):
	return int(os.popen('ifconfig -a | grep '+nic_id+' | wc -l').read())!=1

def config():
	global net_interface,secondary_net_interface
	
	if check_if_nic_exists(net_interface):
		print net_interface+' NOT found!!'
		exit(-1)
	if check_if_nic_exists(secondary_net_interface):
		print secondary_net_interface+' NOT found!!'
		exit(-1)

	os.popen('echo 0 > /proc/sys/net/ipv4/ip_forward')	#disable ipv4 forwarding to be a _blackhole_
	os.popen('service network-manager stop')	#stop nm or it will interfere with our operations
	
	os.popen('ifconfig '+net_interface+' up')
	os.popen('ifconfig '+secondary_net_interface+' up')

def main():
	if os.geteuid() != 0:
		print 'This program must be run as root [RAW sockets, Kernel property settings, ifconfig ... ]' #using flag SOCK_RAW on syscall
		exit(-1)	

	config()

	while True:
		scan()
		time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()