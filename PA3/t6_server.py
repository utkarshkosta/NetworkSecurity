import socket
import pickle

ip = '127.0.0.1'
port = 12345

s = socket.socket()
s.bind((ip, port))
s.listen(1)

c,a = s.accept()

# #FOR IMAGE
# f = open('withHiddenMsg.png', 'rb')
# image = f.read()
# data = pickle.dumps(image)
# c.send(data)

#FOR VIDEO
f = open('msgHidden.avi','rb')
video = f.read()
data = pickle.dumps(video)
c.send(data)

s.close()
c.close()

ip = '127.0.0.2'
port = 12345

s = socket.socket()
s.bind((ip, port))
s.listen(1)

c,a = s.accept()

data = b''
while(1):
	chunk = c.recv(1024 * 50)
	if not chunk:
		break
	data += chunk

data = pickle.loads(data)
print(data)
s.close()
c.close()
