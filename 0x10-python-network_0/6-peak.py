#!/usr/bin/python3
'''
Module for task 6
'''


# def find_peak(list_of_integers):
#     '''
#     Function to find the peak of a list of integers
#     '''
#     if list_of_integers == []:
#         return None
#     current_index = len(list_of_integers)//2
#     peak = list_of_integers[current_index]
#     prev = current_index - 1
#     next = current_index + 1

#     while (prev >= 0 and next <= len(list_of_integers) - 1):
#         if (list_of_integers[prev] > peak):
#             peak = list_of_integers[prev]

#         if (list_of_integers[next] > peak):
#             peak = list_of_integers[next]
#         prev -= 1
#         next += 1

#     while (prev >= 0):
#         if (list_of_integers[prev] > peak):
#             peak = list_of_integers[prev]
#         prev -= 1

#     while (next < len(list_of_integers)):
#         if (list_of_integers[next] > peak):
#             peak = list_of_integers[next]
#         next += 1
#     # print(peak)
#     return peak


def recurse(my_list, start, end):
    if start == end:
        return my_list[start]
    if end - start == 1:
        if my_list[end] > my_list[start]:
            return my_list[end]
        else:
            return my_list[start]

    mid = (start + end) // 2
    left = recurse(my_list, start, mid - 1)
    right = recurse(my_list, mid + 1, end)

    if (my_list[mid] > left and my_list[mid] > right):
        return my_list[mid]
    elif left > my_list[mid] and left > right:
        return left
    else:
        return right


def find_peak(list_of_integers):
    '''
    Function to find the peak of a list of integers
    '''
    if list_of_integers == []:
        return None

    return recurse(list_of_integers, 0, len(list_of_integers) - 1)
