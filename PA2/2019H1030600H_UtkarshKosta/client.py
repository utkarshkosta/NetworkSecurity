import socket
import pickle
import sys
import os
import json
import rsa

def register(ip_addr, port_no, userid, password, e1, n1):
	s = socket.socket()
	s.connect((ip_addr, port_no))
	public_key = [e1,n1]
	data = pickle.dumps({'username' : userid, 'password' : password, 'pk' : public_key})
	s.send(data)
	s.close()


if __name__=='__main__':
	
	buff = []

	if len(sys.argv) != 3:
		print("Usage : python3 client.py <username> <password>")
		exit()
	ip = '127.0.0.1'
	port = 12345
	username = sys.argv[1]
	password = sys.argv[2]
	vals = []
	if(os.path.exists(username)):
		keys = open(username, 'r')
		vals = json.load(keys)
		keys.close()
		print(vals)
	else:
		e,d,n = rsa.generate_keys()
		vals = [e,d,n]
		keys = open(username, 'w')
		json.dump(vals, keys)
		keys.close()
		print(vals)

	register(ip, port, username, password, vals[0], vals[2])
