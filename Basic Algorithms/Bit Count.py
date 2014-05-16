import binascii

__author__ = 'Irrevocable Cascade'

"""As you probably know, all values inside a computer are represented in binary system. In this simple task you are to
write a program which counts the number of non-zero bits in a given value.

For example:

value             binary                count
  1   00000000000000000000000000000001      1
100   00000000000000000000000001100100      3
 -1   11111111111111111111111111111111     32

Input data will contain a number of values to process.
Next line will contain the values themselves, each in range -2 000 000 000 .. 2 000 000 000.
Answer should contain the counts of bits set to 1 for each of values, separated by spaces."""

def bit_count(filename):
	with open(filename) as file:
		list = file.read().split()

	result = []

	tobin = lambda x, count=32: "".join(map(lambda y: str((x >> y) & 1), range(count - 1, -1, -1)))

	for number in list:
		print(tobin(int(number)))
		result.append(tobin(int(number)).count('1'))

	return result


print(bit_count('bit_count.txt'))