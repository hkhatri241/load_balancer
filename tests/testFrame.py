import unittest
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) #kind of hack make a package with __init__.py and use relative imports
from frame import Frame

class frameTestCase(unittest.TestCase):
    """Tests for frame.py."""

    def test_isIPRequest(self):
        testFrame ='\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0\xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
        frame = Frame(testFrame)
        self.assertTrue(frame.isIPRequest())

    def test_getDestMac(self):
        testFrame = '\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0\xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
        frame = Frame(testFrame)
        self.assertEqual(frame.getDestMac(), '00021537a244')

    def test_getSourceMac(self):
        testFrame = '\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0\xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
        frame = Frame(testFrame)
        self.assertEqual(frame.getSourceMac(), '00aef352aad1')

    def test_getSourceIP(self):
        testFrame = '\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0\xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
        frame = Frame(testFrame)
        self.assertEqual(frame.getSourceIP(), '192.168.5.21')

    def test_getDestIP(self):
        testFrame = '\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0\xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
        frame = Frame(testFrame)
        self.assertEqual(frame.getDestIP(), '66.35.250.151')


if __name__ == '__main__':
    unittest.main()
