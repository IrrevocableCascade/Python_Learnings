___author__ = 'Irrevocable Cascade'

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def is_prime(n):
	n = abs(int(n))

	if n < 2:
		return False

	if n == 2:
		return True

	if not n & 1:
		return False
	for x in range(3, int(n ** 0.5) + 1, 2):
		if n % x == 0:
			return False
	return True

total = 0

for i in range(2000000):
	if is_prime(i):
		total += i

print("FINAL: {0}".format(total))