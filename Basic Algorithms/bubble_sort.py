__author__ = 'Irrevocable Cascade'

"""Array sorting is a popular problem for programming newcomers - and extremely important thing in professional
programming (in databases, libraries etc).

Sorting is reordering according to some simple rule based on comparison. Suppose we are given an array:

a = [3, 1, 4, 1, 5, 9, 2, 6]
and we want its elements to be reordered in non-decreasing order - i.e. if one element is placed earlier (to the left)
than the other - we can be sure the first element is either less or equal to second.

Mathematically speaking, for any indexes i and j if i < j then a[i] <= a[j].

Bubble Sort is one of the simplest methods to perform such reordering. We will describe it in even simpler way than
usual:

Take a pass through array, examining all pairs of adjacent elements (N-1 pairs for array of N elements).
If in any pair with indexes i and i+1 the condition a[i] <= a[i+1] does not hold, swap these two elements.
Repeat such passes through array until the new pass will do no swaps at all.
It is obvious, that if the pass do not perform any swaps, the array is already sorted and future passes could not change
anything."""


def bubbleSort(alist):
	exchanges = True
	passnum = len(alist) - 1
	exchanges_counter = 0
	passes_counter = 0

	while passnum > 0 and exchanges:
		exchanges = False

		for i in range(passnum):
			if int(alist[i]) > int(alist[i + 1]):
				exchanges = True
				exchanges_counter += 1
				temp = alist[i]
				alist[i] = alist[i + 1]
				alist[i + 1] = temp

		passnum -= 1
		passes_counter += 1

	return alist, passes_counter, exchanges_counter


def bubble_sort(filename):
	with open(filename) as file:
		bubble_list = file.read().split()

	print(bubbleSort(bubble_list))


print(bubble_sort('values.txt'))