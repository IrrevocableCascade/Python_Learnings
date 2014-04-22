__author__ = 'Irrevocable Cascade'

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def find_factors(number):
	i = 1
	factors = []
	result = 0
	while i < 10000000:
		if number % i == 0:
			result = int(number / i)
			factors.append(i)
			factors.append(result)
		i += 1
	return factors


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


factors = set(find_factors(600851475143))

print(factors)
prime_factors = []

for i in factors:
	print("Working on {0}".format(i))
	if is_prime(i):
		prime_factors.append(i)

print(prime_factors)