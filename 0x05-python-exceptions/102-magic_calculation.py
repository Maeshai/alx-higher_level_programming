#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise ValueError('Value of i is too large')
            else:
                res += (a ** b) / x
        except ValueError:
            res = b + a
            break
    return res
