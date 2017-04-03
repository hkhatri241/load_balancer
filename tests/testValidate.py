import unittest
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) #kind of hack make a package with __init__.py and use relative imports
from validate import Validate

class validateTestCase(unittest.TestCase):
    """Tests for frame.py."""

    def test_isValidIP(self):

        correctIp = ['172.31.2.7','1.2','0.0']

        for ip in correctIp:
            errorMsg = ip + " is not valid."
            self.assertTrue(Validate.isValidIP(ip),msg = errorMsg)

        incorrectIp = ['1.a.2.3','0.0.']

        for ip in incorrectIp:
            errorMsg = ip + " is not valid."
            self.assertFalse(Validate.isValidIP(ip),msg = errorMsg)

    def test_isValidPort(self):
        
        validPorts = [2,3,87,35589]
        for port in validPorts:
            errorMsg = str(port) + " is not valid."
            self.assertTrue(Validate.isValidPort(port),msg = errorMsg)

        inValidPorts = [0,'af',76666]

        for port in inValidPorts:
            errorMsg = str(port) + " is not valid."
            self.assertFalse(Validate.isValidPort(port),msg = errorMsg)

    def test_isInterfaceUp(self):
        
        pass

    

if __name__ == '__main__':
    unittest.main()
