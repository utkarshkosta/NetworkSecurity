import socket
import numpy as np
import pickle
import time

ip = '127.0.0.1'
port = 12345

s = socket.socket()
s.connect((ip, port))
f = open('sample.mp3', 'rb')
audio = f.read()
data = pickle.dumps(audio)
s.send(data)
# time.sleep(2)

# flag = s.recv(1)

s.close()

time.sleep(2)

ip = '127.0.0.2'
port = 12345

s = socket.socket()
s.connect((ip, port))
f = open('sample.avi', 'rb')
video = f.read()
data = pickle.dumps(video)
s.send(data)
