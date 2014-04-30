__author__ = 'http://interactivepython.org/'

"""Selection sort is an in-place comparison sort. It has O(n2) complexity, making it inefficient on large lists, and
generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and also has
performance advantages over more complicated algorithms in certain situations.

The algorithm finds the maximum value, swaps it with the value in the last position, and repeats these steps for the
remainder of the list. It does no more than n swaps, and thus is useful where swapping is very expensive."""


def selection_sort(alist):
	for fillslot in range(len(alist) - 1, 0, -1):
		positionOfMax = 0
		for location in range(1, fillslot + 1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp


alist = [1, 13, 56, 78, 33, 49, 134, 44, 234566, 2221, 234, 1, 4456, 6788666, 33, 222, 111, 23, 3, 4, 56, 11, 77, 44, 55
	, 66, 77, 88, 45678902, 123311]
selection_sort(alist)
print(alist)









