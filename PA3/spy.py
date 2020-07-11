import captureVideo as cv
import captureAudio as ca
import cv2
import sounddevice as sd
import numpy as np
from multiprocessing import Process
import keyLogger as k
import time
from  pynput import keyboard

record = []

# duration = 5
duration = 10

def video():
	global duration
	print("Recording Video...")
	cap = cv2.VideoCapture(0)
	width = int(cap.get(3))
	height = int(cap.get(4))
	out = cv2.VideoWriter('recordedVideo.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))
	# print(type(out))
	frames = cv.record_video(duration, cap)
	for frame in frames:
		out.write(frame)
	cap.release()
	out.release()
	cv2.destroyAllWindows()


def audio():
	print("Recording Audio...")
	global duration
	recording = ca.record_audio(duration)
	np.save("recordedAudio", recording)
	# sd.play(recording)
	# sd.wait()

def keys():
	print("Recording keylog...")
	global duration
	key_log = k.record_key_press(duration)
	f = open('keylog.txt', 'w')
	for key in key_log:
		f.write(key)
		f.write("\n")


if __name__ == '__main__':
	p1 = Process(target = video)
	p2 = Process(target = audio())
	p3 = Process(target = keys)
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()
