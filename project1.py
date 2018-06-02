#!/usr/bin/python2

#import library
import time 		#library to get access of time
import os       	#to access operating system commands 
import webbrowser 	#to get the access of Browsing
import facebook   	#to get access of facebook 
import requests		#to send organic,grass-fed HTTP/1.1	 
import urllib		#for url library
from bs4 import BeautifulSoup  #to wrap the url 

x='''
press 1: show current time
press 2: reboot operating system
press 3: to create a user in your current o.s
press 4: to get the info about RAM and MEMORY
press 5: to get the ip address of all connected device
press 6: to search something on google
press 7: to upload status on facebook
press 8: to get the url of your search
'''
#print option to user
print x							#print option to user

choice = int(raw_input("enter your chocice"))		

if choice == 1:
	#to get current time
	print time.ctime().split()[3]			#to get current time

elif choice == 2:
	#to reboot system
	os.system('reboot')

elif choice == 3:
	
	name = raw_input("enter the user name")
	#to get the user name
	os.system('useradd'+name)
	#to set a password for that user			#to get the user name
	os.system('passwd'+name)			#to set a password for that user

elif choice == 4:
	#to check the ram and memory of system					
	os.system('free -m')				#to check the ram and memory of system

elif choice == 5:
	#to get the system ip address
	os.system('ifconfig')				#to get the system ip address

elif choice == 6:
	url=raw_input("enter your search")
	#to show the search in google
	webbrowser.open_new_tab('https://www.google.com/search?q='+url)			#to show the search in google

elif choice == 7:
	#to get access of user_access_token for facebook and google Api
	graph = facebook.GraphAPI('EAACEdEose0cBAKQl9iXlTsVV24ZBb1SI6HXrQNQFLfrgZB0u28ZAP4VPn7dABwGp54fHgAS2cFzv1ZBCKOJ4C6mGb7CnDIE0LGK1dDv3GjyWLOQZAFxyaoOm1M6E9k2o3VdE91E16HADWAY2D2gYuDSDDMS6YmjYsddlwjofGwVspcbJ0Bjlfn33tCLfKQIw9jRJZB3hRSowZDZD', version="2.12")						#to get access of user_access_token for facebook and google Api
	status=raw_input("enter your status")
	#to post the status on user facebook
	graph.put_object(parent_object='me', connection_name='feed', message=status)	#to post the status on user facebook
                                              
	
elif choice == 8:
	text = raw_input("enter your search")
	text = urllib.quote_plus(text)

	url = 'https://google.com/search?q=' + text
	
	#to get response from the url
	response = requests.get(url)

	#to wrap the url
	soup = BeautifulSoup(response.text, 'lxml')
	for g in soup.find_all(class_='g'):
		#to print url
    		print(g.text)
    		print('-----')

else:
	print "enter the correct choice"
	
	 
