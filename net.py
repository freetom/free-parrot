class net:
	def __init__(self, descriptor_str):
		#print descriptor_str

		i=descriptor_str.index('Address')+len('Address')+2
		self.ap_mac=descriptor_str[i:i+17]

		i=descriptor_str.index('Signal level')+len('Signal level')+1
		j=descriptor_str[i:].index(" ")
		self.rx_power=descriptor_str[i:i+j]

		i=descriptor_str.index('ESSID')+len('ESSID')+2
		j=descriptor_str[i:].index("\"")
		self.essid=descriptor_str[i:i+j]

		print "Net -> "+self.ap_mac+" "+self.rx_power+" "+self.essid
