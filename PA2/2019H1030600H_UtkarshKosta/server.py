import socket
import pickle
import hashlib
import json

ip = '127.0.0.1'
port = 12345
registry = []

def display_table(table):
	for i in range(len(table)):
		print("Username : ",table[i][0])
		print("Password hash : ",table[i][1])
		print("Public key : ",table[i][2])
		if(i != len(table) - 1):
			print("\n")

s = socket.socket()
s.bind((ip,port))
# num_of_clients = 2
while(1):
	buff = []
	s.listen(1)
	c, a = s.accept()
	buff = c.recv(1024)
	details = pickle.loads(buff)
	# print(details)
	m = hashlib.sha256()
	m.update(details['password'].encode('utf-8'))
	hash_val = m.hexdigest()
	temp = [details['username'], hash_val, details['pk']]
	if temp in registry:
		display_table(registry)
		print("------------------------------------------------------------")
		continue
	else:
		registry.append(temp)
		display_table(registry)
		print("------------------------------------------------------------")
s.close()


	# print(pickle.loads(buff))
	# print(c)
	# print(a)
