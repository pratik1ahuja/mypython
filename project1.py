#!/usr/bin/python2

import time 	#for time lib.
import os
import webbrowser 
import facebook 	 #for os lib.

x='''
press 1: show current time
press 2: reboot operating system
press 3: to create a user in your current o.s
press 4: to get the info about RAM and MEMORY
press 5: to get the ip address of all connected device
press 6: to search something on google
press 7: to upload status on facebook
'''

print x

choice = int(raw_input("enter your chocice"))	#to get input rom user

if choice == 1:
	print time.ctime().split()[3]		#to get current time

elif choice == 2:
	os.system('cal')

elif choice == 3:
	
	name = raw_input("enter the user name")
	os.system('useradd'+name)
	#pss = raw_input("enter the password")
	os.system('passwd'+name)			#to add user in os

elif choice == 4:
	os.system('free -m')

elif choice == 5:
	os.system('ifconfig')

elif choice == 6:
	url=raw_input("enter your search")
	webbrowser.open_new_tab('https://www.google.com/search?q='+url)

elif choice == 7:
	graph = facebook.GraphAPI('EAACEdEose0cBAKQl9iXlTsVV24ZBb1SI6HXrQNQFLfrgZB0u28ZAP4VPn7dABwGp54fHgAS2cFzv1ZBCKOJ4C6mGb7CnDIE0LGK1dDv3GjyWLOQZAFxyaoOm1M6E9k2o3VdE91E16HADWAY2D2gYuDSDDMS6YmjYsddlwjofGwVspcbJ0Bjlfn33tCLfKQIw9jRJZB3hRSowZDZD', version="2.12")
	status=raw_input("enter your status")
	graph.put_object(parent_object='me', connection_name='feed', message=status)
                                              
	
	

	 
