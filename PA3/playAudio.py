import sounddevice as sd
import sys
import numpy as np

if len(sys.argv) != 2:
	print("Usage : python3 playAudio.py <audioFile>.npy")
	exit()

audioFile = sys.argv[1]
audio = np.load(audioFile)
print("Playing audio...")
sd.play(audio)
sd.wait()
