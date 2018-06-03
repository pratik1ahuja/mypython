#!/usr/bin/python2

#import modeule
import socket
import os

#for make connection between sender and receiver
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#for binding the network 
s.bind(("127.0.0.1",7777))

for i in range(10000):
	#to get the data from sender side
	data = s.recvfrom(10000)
	print data
	#to give the message to sender in voice form
	msg = os.system('echo "hii" | festival --tts')
	#to send message to sender
	s.sendto(str(msg),data[1])
	
	
