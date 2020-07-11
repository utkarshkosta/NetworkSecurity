import sounddevice as sd

# duration = 10

def record_audio(duration):
	sampling_freq = 44100
	sd.default.samplerate = sampling_freq
	sd.default.channels = 2
	recording = sd.rec(int(duration * sampling_freq))
	# print("Recording...")
	sd.wait()
	return recording


if __name__=='__main__':
	recorded = record_audio(5)
	print("Playing recorded audio...")
	sd.play(recorded)
	# print(type(recording))
	sd.wait()