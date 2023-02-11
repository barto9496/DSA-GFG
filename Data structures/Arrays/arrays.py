# Code for finding 3 largest elements in an array

# Problem Statement: Given an array with all distinct elements, find the largest three elements.
# Expected time complexity is O(n) and extra space is O(1)

# Python3 code to find largest three
# elements in an array

# Solution: or implementation analysis: What you can do for this is assign the largest negative value to all the three
# variables, the advantage with that is you have the largest negative numbers which need to be compared with the rest of the
# elements and if that element is given in array then never mind. So with that being said the next thing we need to do is
# compare the elements for the comparison what we need to do is we need compare the first one with the next array if it is the largest
# change the order of elements by assigning second to the third one and third to the second one and the greatest value element to the first
# if not then check for the second and third element


import sys


def print3largest(arr, arr_size):
    third = second = first = -sys.maxsize
    if arr_size < 3:
        print("Invalid input")
        return

    for i in range(0, arr_size):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second:
            third = second
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]

    print("The three largest elements in the array are:", first, second, third)


arr = [12, 14, 1, 144, 71]
n = len(arr)
print3largest(arr, n)


# Couple of variations:


def print3Smallest(arr, n):
    third = second = first = sys.maxsize
    for i in range(0, n):
        if arr[i] < first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] < second:
            third = second
            second = arr[i]

        elif arr[i] < third:
            third = arr[i]

    print("The smallest 3 numbers are:", first, second, third)

arr1 = [12, 14, 1, 144, 71]
n = len(arr1)
print3Smallest(arr1, n)
