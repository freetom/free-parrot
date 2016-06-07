import time
import os

from monitor import *
from global_vars import *

def config():
	os.popen('echo 0 > /proc/sys/net/ipv4/ip_forward')	#disable ipv4 forwarding to be a _blackhole_
	os.popen('service network-manager stop')	#stop nm or it will interfere with our operations
	os.popen('ifconfig '+net_interface+' up')

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