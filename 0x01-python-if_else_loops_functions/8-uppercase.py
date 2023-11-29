#!/usr/bin/python3
def to_upper(character):
    if 'a' <= character <= 'z':
        return ord(character) - ord('a') + ord('A')
    else:
        return ord(character)

def uppercase(string):
    string_new = "".join(chr(to_upper(char)) for char in string)
    print(string_new)

# Example usage:
uppercase("Hello, World!")
