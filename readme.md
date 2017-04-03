Points to note:
Place the config file in /etc/ in ubuntu.
Validate.py has not been run. May break.(will be finished in a couple of hours)
Everything fails silently i.e. exceptions are catched ,logged and system exits.
Server checkup using ping at the start of the load balancer will be done in couple of hours.
Test cases will be done in a couple of hours.

Documentation:
frame.py- 
Use - from frame import Frame
Accepts a raw packet from socket.recv()
Methods:
	isIPRequest() - Returns true if an ip request.
		getDestIPAddr() - returns destination ip address if an ip request.String of format  "1.2.3.4"
		getSourceIpAddr() - returns source ip address if an ip request.String of format "2.3.4.5"

	isARPRequest() - Returns true if an arp request.

	getSourceAddr - returns source mac address.Return value - 2356af15eb53 if mac address is 23-56-af-15-eb-53(hex 				format).Therefore, do parse it yourparams.

	getDestAddr() - returns destination mac address. Return value - 2356af15eb53 if mac address is 23-56-af-15-eb-53(hex 				format).Therefore, do parse it yourparams.


params.py-
Use - fro params import Params

Simply instantiate as params = Params().
Cofig file reading , empty checking and ip,port and interface validation is taken care of.
Note - Only checks whether port no is valid( lies between 0 and 65535). When opening a socket connection, port may not open. Catch that 	exception in the main loop.
To access config properties-
	params.vip_interface  - eth0 or virtual0 etc
    	params.vip_port 
    	params.vip_ip 
    	params.target_ip - Array of Target ips. See config file for an example.
    	params.load_balancer_algorithm = Integer value. No checks on it. Discuss the algorithms to be implemented

validate.py - 
Class with static / class methods used by params.py
Do not use directly.

