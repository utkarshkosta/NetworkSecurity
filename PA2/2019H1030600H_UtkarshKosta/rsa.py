import sys
import random as r
import math as m

MAX = 100

def isPrime(a):
	for i in range(2,a):
		if (a % i) == 0:
			return False
	return True

def generate_keys():
	p = r.randint(2, MAX)
	while(not isPrime(p)):
		p = r.randint(2, MAX)

	q = r.randint(2, MAX)
	while(not isPrime(q)):
		q = r.randint(2, MAX)

	n1 = p * q

	phi_n = (p-1) * (q-1)

	e1 = r.randint(2, phi_n)
	while(m.gcd(e1,phi_n) != 1):
		e1 = r.randint(2, phi_n)

	k = 1
	d1 = float(phi_n * k + 1) / float(e1)
	while(d1 != int(d1)):
		k += 1
		d1 = float(phi_n * k + 1) / float(e1)
	d1 = int(d1)

	while(e1 == d1):
		e1,d1,n1 = generate_keys()

	return e1,d1,n1

def encrypt(d,n, byte_stream):
	cipher_text_list = []
	cipiher_text_int = 0

	if type(byte_stream) == int:
		cipher_text_int = (byte_stream ** d) % n
		# print(cipher_text_int)
		return cipher_text_int
	else:
		for i in range(len(byte_stream)):
			cipher_text_list.append((byte_stream[i] ** d) % n)
		print(cipher_text_list)
		return cipher_text_list

def decrypt(e,n, cipher_text):
	deciphered_text_list = []
	deciphered_text_int = 0

	if type(cipher_text) == int:
		deciphered_text_int = (cipher_text ** e) % n
		return deciphered_text_int
	else:
		for i in range(len(cipher_text)):
			deciphered_text_list.append((cipher_text[i] ** e) % n)
		return deciphered_text_list


# def debug():
# 	print(k)
# 	print(p)
# 	print(isPrime(p))
# 	print(q)
# 	print(isPrime(q))
# 	print(n)
# 	print(phi_n)
# 	print(e)
# 	if(n%e == 0):
# 		print("False")
# 	else:
# 		print("True")
# 	print(d)

if __name__=='__main__':
	if len(sys.argv) != 2:
		print("Usage : python3 filename.py <source_file_path> <destination_file_path>")
		exit()
	source_file = sys.argv[1]
	destination_file = 'deciphered_file'
	f1 = open(source_file,'rb')
	f2 = open(destination_file, 'w')
	byte_stream = f1.read()
	# print(byte_stream)
	e,d,n = generate_keys()
	cipher_text = encrypt(d,n, byte_stream)
	deciphered_text = decrypt(e,n, cipher_text)
	for i in range(len(deciphered_text)):
		# deciphered_text[i] = deciphered_text[i].to_bytes(8, byteorder = 'big')
		# print(chr(deciphered_text[i]))
		f2.write(chr(deciphered_text[i]))
	# print(deciphered_text)
