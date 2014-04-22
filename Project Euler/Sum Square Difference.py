__author__ = 'Irrevocable Cascade'

"""The sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


def sum_of_squares(number):
	total = 0

	for i in range(1, number + 1):
		total += i * i

	return total

def square_of_sum(number):
	total = 0

	for i in range(1, number +1):
		total += i

	return total * total

n = sum_of_squares(100)
m = square_of_sum(100)
print("Difference is {0}".format(m - n))