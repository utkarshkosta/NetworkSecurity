import socket
import pickle
import sounddevice as sd
import numpy as np

ip = '127.0.0.1'
port = 12345


s = socket.socket()
s.bind((ip, port))
s.listen(1)
c,a = s.accept()

audio_fragments = b''

while(1):
	chunk = c.recv(1024)
	if not chunk:
		break
	audio_fragments += chunk
	# print(chunk)

audio = pickle.loads(audio_fragments)
print("Audio file received...")
with open('receivedAudio.mp3', 'wb') as f:
	f.write(audio)
# sd.play(audio)
# sd.wait()
s.close()


ip = '127.0.0.2'
port = 12345

s = socket.socket()
s.bind((ip, port))
s.listen(1)
c,a = s.accept()

video_fragments = b''
while(1):
	chunk = c.recv(1024)
	if not chunk:
		break
	video_fragments += chunk

video = pickle.loads(video_fragments)
print("Video file received...")

with open('receivedVideo.avi', 'wb') as f:
	f.write(video)

s.close()



# print(audio)
