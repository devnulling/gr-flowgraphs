import pyaudio
import wave
import sys
import time
import struct
import socket
from struct import *
CHUNK=32768

p = pyaudio.PyAudio()

count = p.get_device_count()
devices = []
for i in range(count):
    devices.append(p.get_device_info_by_index(i))

for i, dev in enumerate(devices):
    print ("%d – %s" % (i, dev['name']))

FORMAT=pyaudio.paFloat32
CHANNELS=2
RATE=96000

input_device_index=0
output_device_index=5
dst = p.open(format = FORMAT,channels = CHANNELS,rate = RATE,output = True,output_device_index = output_device_index,frames_per_buffer = CHUNK)

UDP_IP = "127.0.0.1"
UDP_PORT = 30000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:   
    data, addr = sock.recvfrom(CHUNK)
    dst.write(data)
