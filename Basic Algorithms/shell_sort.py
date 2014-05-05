__author__ = 'Irrevocable Cascade & interactivepython.org'


def shell_sort(alist):
    gap = 3
    sub_list_one = []
    sub_list_two = []
    sub_list_three = []

    for item in range(0, len(alist), gap):
        sub_list_one.append(alist[item])
        sub_list_two.append(alist[item + 1])
        sub_list_three.append(alist[item + 2])

    insertionSort(sub_list_one)
    insertionSort(sub_list_two)
    insertionSort(sub_list_three)

    print(sub_list_one)
    print(sub_list_two)
    print(sub_list_three)

    alist = sub_list_one + sub_list_two + sub_list_three
    insertionSort(alist)
    print(alist)


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
