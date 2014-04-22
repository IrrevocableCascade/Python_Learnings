__author__ = 'Irrevocable Cascade'

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""


def is_prime(n):
	'''check if integer n is a prime'''
	# make sure n is a positive integer
	n = abs(int(n))
	# 0 and 1 are not primes
	if n < 2:
		return False
	# 2 is the only even prime number
	if n == 2:
		return True
		# all other even numbers are not primes
	if not n & 1:
		return False
	# range starts with 3 and only needs to go up the squareroot of n
	# for all odd numbers
	for x in range(3, int(n ** 0.5) + 1, 2):
		if n % x == 0:
			return False
	return True


j = 0

for i in range(2, 300000):

	if is_prime(i):
		j += 1
		print("Prime found: {0}".format(i))
		print(str(j))
		if j == 10001:
			print("The 10001st prime number is {0}".format(i))
			break
