__author__ = 'Irrevocable Cascade'

"""Bubble sort, sometimes incorrectly referred to as sinking sort, is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted,
comparing each pair of adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until n - 1 passes have been completed or no swaps have been done."""


def bubble_sort(alist):
	swapped = True
	passes = len(alist) - 1

	while passes > 0 and swapped:
		swapped = False
		for i in range(len(alist) - 1):
			if alist[i] > alist[i + 1]:
				temp = alist[i + 1]
				alist[i + 1] = alist[i]
				alist[i] = temp
				swapped = True
		passes -= 1

alist = [1, 13, 56, 78, 33, 49, 134, 44, 234566, 2221, 234, 1, 4456, 6788666, 33, 222, 111, 23, 3, 4, 56, 11, 77, 44, 55
	, 66, 77, 88, 45678902, 123311,]
bubble_sort(alist)
print(alist)
