#!/bin/python

import sys
import socket 
from datetime import datetime

# define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # translate hostname to ipv4
else:
	print("Invalid Amount of arguments.")
	print("Synatx: python3 port_scanner.py <ip>")

# add banner
print("-" * 50)
print("Scanning target " + target)
print("Time Started: "+ str(datetime.now()))
print("-" * 50)

try:
	for port in range(1, 80):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("Exiting Program ...")
	sys.exit()

except socket.gaierror:
	print("Hostname could not resolve ...")
	sys.exit()

except socket.error:
	print("Couldn't connect to server ...")
	sys.exit()