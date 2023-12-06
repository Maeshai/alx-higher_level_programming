#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
