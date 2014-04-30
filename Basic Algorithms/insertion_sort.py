__author__ = 'http://interactivepython.org/'

"""Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is
much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However,
insertion sort provides several advantages:

Simple implementation
Efficient for (quite) small data sets
Adaptive (i.e., efficient) for data sets that are already substantially sorted: the time complexity is O(n + d), where d is the number of inversions
More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort; the best case (nearly sorted input) is O(n)
Stable; i.e., does not change the relative order of elements with equal keys
In-place; i.e., only requires a constant amount O(1) of additional memory space
Online; i.e., can sort a list as it receives it"""


def insertion_sort(alist):
	for index in range(1, len(alist)):

		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position -= 1

		alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)