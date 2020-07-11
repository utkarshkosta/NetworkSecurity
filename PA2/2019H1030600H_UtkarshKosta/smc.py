import rsa
import math as m
import random as r
import time

# f1 = open("f1.txt", 'r')
# f2 = open("f2.txt", 'r')

# x = int(f1.read())
# y = int(f2.read())
x = r.randint(1,100)
y = r.randint(1,100)
N = 100

def condition_check(zlist, prime):
	# print("prime selected : ",prime)
	for i in range(len(zlist)):
		if zlist[i] > 0 and zlist[i] < prime - 1:
			continue
		else:
			return False

	for i in range(0, len(zlist)-1):
		for j in range(i+1, len(zlist)):
			x =  abs(zlist[i] - zlist[j])
			# print("z[",i,"] - z[",j,"] = ",x)
			# print(x)
			if x >= 2:
				continue
			else:
				return False

	return True

def pick_prime():
	prime_list = []
	# prime = r.randint(3,m1)
	# while(not rsa.isPrime(prime)):
	# 	prime = r.randint(3,m1)

	for i in range(3,511):
		if rsa.isPrime(i):
			prime_list.append(i)

	return prime_list

def compute_zlist(p, range_numbers, m2list):
	computed_zlist = []
	for i in range(0,range_numbers):
		computed_zlist.append(m2list[i] % p)
	return computed_zlist


def secure_two_party_computation():

	global x,y,N

	e,d,n = rsa.generate_keys()
	# e,d,n = 7,23,55
	print("keys (e,d,n) : ", e,d,n)
	while(n < 1024):
		time.sleep(1)
		e,d,n = rsa.generate_keys()
		print("Reselected keys (e,d,n) : ", e,d,n)


	m1 = r.randint(512,1024)
	# m1 = 39
	print("m1 : ",m1)

	# size_of_m1 = math.log(m1, 2)
	# print("size of m1 : ",size_of_m1)

	c = rsa.encrypt(e, n, m1)
	c1 = c - x
	print("c1 : ",c1)

	m2 = []
	for i in range(1,N+1):
		m2.append(rsa.decrypt(d, n, c1+i))

	# print("m2 : ",m2)

	p = pick_prime()
	# p = 31
	selected = 0
	# print("Prime list : ",p)
	for i in range(len(p)):
		selected = p[i]
		z = compute_zlist(selected, N, m2)
		# print("z : ",z)
		f = condition_check(z,selected)
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

	# print(p)
	if (z[x-1] % selected) == (m1 % selected):
		return "x <= y"
	else:
		return "x > y"


if __name__=='__main__':
	result = secure_two_party_computation()
	print(result, "(x :",x,", y :",y,")")
