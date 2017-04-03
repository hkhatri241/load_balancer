from IPy import IP
import os

class Validate():

    
    def __init__(self):
        pass
        

    @classmethod
    def isValidIP(cls, ip):
        try:
            IP(ip)  #simple
            return True
        except ValueError:
            return False


    @classmethod    
    def isValidPort(cls, port):

        try:
            isValid = int(port) >0 and int(port) <=65535  #whether port is free and can be opened is to checked in main loop
        except ValueError:
            print("Port number is not an integer")
            return False

        return isValid

    @classmethod
    def isInterfaceUp(cls, interface):
        #http://stackoverflow.com/questions/3837069/how-to-get-network-interface-card-names-in-python
        #as seen above,cleaner methods exist
        #module named netifaces,however may be overkill for this job,hence not using.

        interface = interface.encode('UTF-8') #interface is unicode,this takes care of it
        
        for x in os.listdir('/sys/class/net/'):
            if interface == x:
            	#print interface + 'is up'
                return True

        return False


    