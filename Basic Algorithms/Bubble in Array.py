__author__ = 'Irrevocable Cascade'

"""This problem provides an exercise for learning core idea of infamous ordering algorithm - bubble sort - which you
are supposed to program bit later.

Given integer array, you are to iterate through all pairs of neighbor elements, starting from beginning - and swap
members of each pair where first element is greater than second.

For example, let us consider small array of elements 1 4 2 3 6 5, marking which pairs are swapped and which are not:

(1  4) 3  2  6  5  - pass
 1 (4  3) 2  6  5  - swap
 1  3 (4  2) 6  5  - swap
 1  3  2 (4  6) 5  - pass
 1  3  2  4 (6  5) - swap
 1  3  2  4  5  6  - end
This operation moves some greater elements right (to the end of array) and some smaller elements left.
What is the most important: biggest element in necessarily moved to the last position.

Input data contain sequence of elements of the array terminated by -1 (which should not be included).
Answer should contain two values - number of performed swaps and checksum of the array after processing
(separated by spaces). Checksum should be calculated with exactly the same method as in the task Array Checksum."""


#TODO I have no idea why this doesnt work holy shit o_O

def checksum(list):
    result = 0
    for item in list:
        result = (((result + int(item)) * 113) % 10000007)

    return result

def bubbleSort_passes(alist):
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

    return alist, passes_counter

def bubble_swap_checksum(filename):

    with open(filename) as file:
        bubble_list = file.read().split()

    print(bubbleSort_passes(bubble_list))
    print(checksum(bubble_list))

print(bubble_swap_checksum('values.txt'))
