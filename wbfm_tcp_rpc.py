#!/usr/bin/env python2
import xmlrpclib
import time
import sys

freq = int(sys.argv[1])

xml = xmlrpclib.Server('http://192.168.1.10:31186');


xml.set_freq(freq)
