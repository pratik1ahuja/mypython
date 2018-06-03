#!/usr/bin/python2

#import modeule
import socket
import os
import commands

#for make connection between sender and receiver
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#for binding the network 
s.bind(("127.0.0.1",7777))

for i in range(10000):
	#to get the data from sender side
	data = s.recvfrom(10000)
	#to get the output of command
	check=commands.getstatusoutput(data[0])
	if check==0:
		#to send the command output to sender
		s.sendto(check[1],data[1])
	else:
		#to send the output if command not found 
		s.sendto(check[1],data[1])
	
	
