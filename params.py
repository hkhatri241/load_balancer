import configparser
from configparser import NoOptionError
import logging
import sys
from validate import Validate

class Params(configparser.ConfigParser):

    
    def __init__(self):
        
        self.vip_interface = None
        self.vip_port = None
        self.vip_ip = None
        self.target_ip = None
        self.load_balancer_algorithm = None
        self.param_list = ['vip_interface','vip_port','vip_ip','target_ip','load_balancer_algorithm']
        self.path = '/etc/load_balancer_config.conf'
        super(Params, self).__init__()  #call ConfigParser's constructor
        self.readConfig()
        self.paramNotEmpty()
        self.validate_params()
        
        

    def readConfig(self):

        if len(self.read(self.path)) == 0:  #config parser does not raise exception when read file;if file does not exist,empty aray is returned.
            self.errorHelper("Config File could not be read.Check if file exists or use root privilege.")

        
        try:
            for x in self.param_list:   #loop through all params and set corresponding properties
                setattr(self, x, self.get('SectionOne', x).strip()) #get rid of any leading,trailing whitespace
        except NoOptionError:
            self.errorHelper("Config Properties not properly set. See Manual. Exiting.")

        setattr(self, 'target_ip', self.target_ip.split(',')) #split target ip string into list of ip's

    def paramNotEmpty(self):
        for param_name in self.param_list:
            if getattr(self,  param_name) == '':
                self.errorHelper("Some properties in config file are empty. Exiting.")
                

    def validate_params(self):

        if not Validate.isValidIP(self.vip_ip):
            self.errorHelper("VIP is not valid. Exiting.")

        for ip in self.target_ip:
            if not Validate.isValidIP(ip):
                self.errorHelper("Target ip are not valid. Exiting.")

        if not Validate.isValidPort(self.vip_port):
            self.errorHelper("Port not valid. Exiting.")


        if not Validate.isInterfaceUp(self.vip_interface):
            self.errorHelper(self.vip_interface+" is not up. Check using ifconfig. Exiting.")


    def errorHelper(self, msg = "some error occured"):#helper function to reduce code redundancy
        print msg
        logging.info(msg)
        sys.exit()
