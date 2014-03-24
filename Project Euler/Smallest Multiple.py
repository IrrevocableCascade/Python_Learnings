__author__ = 'Irrevocable Cascade'

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


def is_evenly_divisible(number):
	i = 1
	while i <= 20:
		if number % i == 0:
			if i == 20:
				return True
			i += 1
			continue
		else:
			break


i = 1

while i <= 1000000000:
	if i % 10000 == 0:
		print('Working on: {0}'.format(i))
	if is_evenly_divisible(i):
		print("Found it: {0}".format(i))
		break
	i += 1
