class net:
	def __init__(self, descriptor_str):
		#print descriptor_str

		i=descriptor_str.index('Address')+len('Address')+2
		self.ap_mac=descriptor_str[i:i+17]

		i=descriptor_str.index('Frequency:')+len('Frequency:')
		j=descriptor_str[i:].index(' ')
		self.frequency=float(descriptor_str[i:i+j])
		self.frequency*=1000.0

		i=descriptor_str.index('ESSID')+len('ESSID')+2
		j=descriptor_str[i:].index("\"")
		self.essid=descriptor_str[i:i+j]

		i=descriptor_str.index('Signal level=')+len('Signal level=')
		j=descriptor_str[i:].index(' ')
		self.rx_power=descriptor_str[i:i+j]

		#if 'ardrone' in self.essid:
		#	print 'Net -> '+self.ap_mac+' '+self.rx_power+'dBm '+self.essid+' '+str(self.frequency)+'Mhz'
