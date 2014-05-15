import itertools

__author__ = 'Irrevocable Cascade'

"""Checksums are small values calculated from big amount of data to test whether data are consistent, i.e. whether they
contain errors.

For example if Anna sends some file to Bob, she can calculate its checksum and tell it Bob, who will calculate checksum
on the file he received, and compare it with the value told by Anna.

For programming several further tasks we'll use similar way to check whether resulting array is correct or not. To avoid
 problems with such tasks let us now practice the checksum calculating algorithm which will be involved.

You will be given the array for which checksum should be calculated. Perform calculation as follows: for each element
of the array (starting from beginning) add this element to result variable and multiply this sum by 113 - this new
value taken by modulo 10000007 should become the next value of result, and so on."""

# 8078463

flatten_iter = itertools.chain.from_iterable

def checksum(list):
	result = 0
	for item in list:
		result = (((result + item) * 113) % 10000007)

	return result


def checksum2(list):
	result = 0
	return ((((result + i) * 113) % 10000007) for i in list)


print(checksum2([96327,77073650,8775,4809,7,63001258,57,648672,97,2121,654,37134902,94244897,10,247,822504,43,596459,9,4,9162448,9,62563,76770,8787304,999311570,75944]))
