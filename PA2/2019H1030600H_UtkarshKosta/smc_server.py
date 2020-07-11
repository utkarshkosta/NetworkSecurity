import socket
import time
import hashlib

ip = '127.0.0.1'
port = 12345

register = []

s = socket.socket()
s.bind((ip,port))
s.listen(1)


numclients = 2
client_list = []
key = ''

def display_register(register):
	for i in range(len(register)):
		print("Username : ", register[i][0])
		print("Password hash : ", register[i][1])
		print("Public key : ", register[i][2])
		if(i != len(register) - 1):
			print("\n")

def register_client(data_received):
	temp = []
	# temp.append(conn)
	for i in range(len(data_received)):
		if(i == 0):
			continue

		if(i != 4):
			if(i == 2):
				m = hashlib.sha256()
				m.update(data_received[i].encode())
				hash_val = m.hexdigest()
				temp.append(hash_val)
			else:
				temp.append(data_received[i])
		else:
	 		break

	if temp in register:
		display_register(register)
		print("------------------------------------------------------------")
	else:
		register.append(temp)
		display_register(register)
		print("------------------------------------------------------------")

def get_public_key(user, reg):
	key = ''
	for i in range(len(reg)):
		if reg[i][0] == user:
			key = reg[i][2]
	return key


received = []
other_user = ''
while(numclients != 0):
	c,a = s.accept()
	numclients -= 1
	# connection_details = [c,a]
	client_list.append(c)
	# print(client_list)
	buff = c.recv(1024)
	buff = buff.decode()
	received = buff.split('|')
	# print(received)

	if 'registration' in received:
		found = 0
		for i in range(len(register)):
			if received[1] == register[i][1]:
				found = 1
		if(not found):
			register_client(received)

	if 'initsmc' in received:
		for i in range(len(received)):
			if(received[i] == 'initsmc'):
				other_user = received[i+1]

key = get_public_key(other_user, register)
# print(key)

if(key):
	client_list[0].send(key.encode())
#time.sleep(2)
c1_byte = client_list[0].recv(1024)
#time.sleep(2)
client_list[1].send(c1_byte)
#time.sleep(2)
z_p_byte = client_list[1].recv(1024)
#time.sleep(2)
client_list[0].send(z_p_byte)
#time.sleep(2)
result = client_list[0].recv(1024)
#time.sleep(2)
client_list[1].send(result)


for i in range(len(client_list)):
	client_list[i].close()
