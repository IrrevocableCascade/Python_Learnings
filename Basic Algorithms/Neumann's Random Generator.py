__author__ = 'Irrevocable Cascade'

"""Random numbers are often used in programming games and scientific researches, but also they could be useful even in business applications (to generate unique user keys, passwords etc.). We are going to learn how they are generated and have a practice with some simple of simpler methods.

Here is one of the earliest methods for producing sequence of seemingly independed (i.e. pseudorandom) numbers:

Choose some initial value with 4 digits (i.e. in range 0000 ... 9999).
Multiply it by itself (i.e. raise to power 2) to get value consisting of 8 digits (add leading zeroes if necessary).
Truncate two first and two last digits in decimal representation of this result.
New value will contain 4 digits and it is the next value of a sequence.
To get more values, repeat from step 2."""


def pseudo_random(seed):

	if len(str(seed)) != 4:
		raise ValueError('Seed not valid, must be 4 digits')

	return str(int(seed) ** 2).zfill(8)[2:6]

def loop_counter(seed):

	count = 1
	results = []
	next_seed = seed

	while True:
		current = pseudo_random(next_seed)

		if current == seed or current in results:
			return count
		else:
			count += 1
		results.append(current)
		next_seed = current


def random_generator(filename):

	with open(filename) as file:
		seed_list = file.read().split()

	return [loop_counter(seed) for seed in seed_list]

print(random_generator("seeds.txt"))


