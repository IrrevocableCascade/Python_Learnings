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


def is_prime(number):
	i = 1
	factors = []
	if number == 2:
		return True
	if number % 2 == 0 or number == 1:
		return False
	else:
		while i < number:
			if number % i == 0:
				factors.append(i)
				if len(factors) > 2:
					return False
			i += 1
	return True


factors = set(find_factors(600851475143))

print(factors)
prime_factors = []

for i in factors:
	print("Working on {0}".format(i))
	if is_prime(i):
		prime_factors.append(i)

print(prime_factors)