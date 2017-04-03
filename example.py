import logging
from params import Params
from frame import Frame
import socket
#from validate import Validate


def main():
    logging.basicConfig(filename='load_balancer.log', level=logging.INFO)
    logging.info('Started')

    #This takes input and validates it
    params = Params()

    #This is how you access the required params
    print params.vip_interface
    print params.vip_port
    print params.vip_ip
    print params.target_ip #do remember that the string eements of the list are in unicode
    print params.load_balancer_algorithm

    #After opening the socket, and receiving the entire packet in sampleFrame
    sampleFrame = '\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0\xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
    
    #Instantiate the frame
    frame = Frame(sampleFrame)


    try:
        s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except ValueError:
        print "cant open socket"
    print 'socket opened'

    s.bind(("virtual0",0))
    print 'socket binded to virtual0'
    
    logging.info('Finished')

if __name__ == '__main__':
    main()