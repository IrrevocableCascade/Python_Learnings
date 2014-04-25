__author__ = 'Irrevocable Cascade'

"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

import random

sum = 0
c = 0

while c < 1000000:

	a = random.randint(1, 1000)
	b = random.randint(1, 1000)
	c = random.randint(1, 1000)
	if a < b < c:
		sum = a + b + c
		if sum == 1000:
			print("Found {0} + {1} + {2}".format(a, b, c))
			if (a ** 2) + (b ** 2) == (c ** 2):
				print("{0} + {1} + {2}".format(a, b, c))
				print(str(a * b * c))
				break
	c += 1
