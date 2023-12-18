#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(0, list_length):
        try:
            div = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
