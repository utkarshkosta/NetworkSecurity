import smc
import time
import socket
import rsa
import os
import json
import sys
import random as r
import pickle

def register(socket, userid, password, pubkey):
	sep = '|'
	data = 'registration' + sep + userid + sep + password + sep + pubkey + sep + 'end' + sep
	socket.send(data.encode())

if __name__ == '__main__':
	ip = '127.0.0.1'
	port = 12345
	userid = sys.argv[1]
	val = sys.argv[2]
	password = '12345'
	sep = '|'
	output = ''
	N = 100

	s = socket.socket()
	s.connect((ip, port))

	vals = []
	if(os.path.exists(userid)):
		keys = open(userid, 'r')
		vals = json.load(keys)
		keys.close()
		# print(vals)
	else:
		e,d,n = rsa.generate_keys()
		while(n < 1024):
			e,d,n = rsa.generate_keys()
		vals = [e,d,n]
		keys = open(userid, 'w')
		json.dump(vals, keys)
		keys.close()
		# print(vals)

	public_key = []
	public_key = str(vals[0])+','+str(vals[2])

	register(s, userid, password, public_key)

	if userid == 'c1':
		x = int(val)
		data = 'initsmc' + sep + 'c2' + sep + 'end'
		s.send(data.encode())
		buff = s.recv(1024)
		# print(buff)
		buff = buff.decode()
		# print(buff)
		other_pk = buff.split(',')
		print("Public key of c2 received : ",other_pk)
		m1 = r.randint(512,1024)
		# m1 = 39
		print("m1 : ",m1)
		# size_of_m1 = math.log(m1, 2)
		# print("size of m1 : ",size_of_m1)
		c = rsa.encrypt(int(other_pk[0]), int(other_pk[1]), m1)
		c1 = c - x
		print("c1 : ",c1)
		s.send(str(c1).encode())
		#time.sleep(2)
		buff = s.recv(1024)
		z_p_final = pickle.loads(buff)
		z_final = z_p_final['z']
		p_final = int(z_p_final['prime'])
		# print(p_final)
		# print(type(p_final))

		if (z_final[x-1] % p_final) == (m1 % p_final):
			result = 'x <= y'
			print(result)
		else:
			result = 'x > y'
			print(result)

		s.send(result.encode())


	if userid == 'c2':
		y = int(val)
		#time.sleep(2)
		c1_byte = s.recv(1024)
		c1 = c1_byte.decode()
		m2 = []
		for i in range(1,N+1):
			m2.append(rsa.decrypt(vals[1], vals[2], int(c1)+i))

		# print("m2 : ",m2)

		p = smc.pick_prime()
		# p = 31
		selected = 0
		# print("Prime list : ",p)
		z = []
		for i in range(len(p)):
			selected = p[i]
			z = smc.compute_zlist(selected, N, m2)
			# print("z : ",z)
			f = smc.condition_check(z,selected)
			if(f):
				break
			else:
				continue
		# z = []
		# z = compute_zlist(p, N, m2)
		# print("z : ",z)
		# while(not condition_check(z, p)):
		# 	print(condition_check(z, p))
		# 	time.sleep(1)
		# 	p = pick_prime(m1)
		# 	z = compute_zlist(p, N, m2)

		for i in range(y, len(z)):
			z[i] += 1


		send_z_p = {'z' : z, 'prime' : selected}
		s.send(pickle.dumps(send_z_p))

		#time.sleep(2)

		result = s.recv(1024)
		result = result.decode()
		print(result)


	s.close()



	# else:
	# 	print("Retry again...")
	# 	exit()
