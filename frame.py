
import socket
from struct import *
import binascii


class Frame(object):

    
    def __init__(self, frame):
        
        self.frame = frame
        self.eth_length = 14
        self.eth_header = self.frame[:self.eth_length]
        self.eth_header = unpack('!6s6s2s' , self.eth_header)
        self.protocol = int(binascii.hexlify(self.eth_header[2]),16)
        self.destAddr = binascii.hexlify(self.eth_header[0])
        self.sourceAddr = binascii.hexlify(self.eth_header[1])
        self.ipHeader = None
        self.arp = None

        if self.protocol == 2048:
            self.ipHeader = unpack("!12s4s4s", self.frame[14:34])#size of ip header is 20 bytes

        if self.protocol == 2054:
            self.arp = self.frame[14:42]# to do unpacking;sze of arp request is 28 bytes
        
        
        

    def isIPRequest(self):
        return self.protocol == 2048

    def isARPRequest(self):
        return self.protocol == 2054

    def getDestMac(self):
        return self.destAddr

    def getSourceMac(self):
        return self.sourceAddr

    def getDestIP(self):
        if self.ipHeader is None:
            return -1

        return socket.inet_ntoa(self.ipHeader[2])#converts to dot format

    def getSourceIP(self):
        if self.ipHeader is None:
            return -1

        return socket.inet_ntoa(self.ipHeader[1])




        




        
