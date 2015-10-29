#!/usr/bin/python3
# coding: UTF-8

import random


def verify_number(my_number):
    assert len(my_number) == 12
    check_digit = calc_check_digit(my_number[:11])
    if my_number[11] == check_digit:
        return True
    else:
        return False


def calc_check_digit(my_number):
    my_number_sum = 0
    assert len(my_number) == 11
    # They count their digits high to low, so reorder it
    my_number_list = my_number[::-1]

    for n in range(1, 7):
        # From digit 1 to 6, sum is n+1
        my_number_sum += (n+1)*my_number_list[n-1]
    for n in range(7, 12):
        # From digit 7 to 11, sum is n-5
        my_number_sum += (n-5)*my_number_list[n-1]

    if my_number_sum % 11 <= 1:
        return 0
    else:
        return 11-my_number_sum % 11


# For testing, generate random "My Number"
def gen_random_number():
    my_number = []
    for n in range(11):
        my_number.append(random.randint(0, 9))
    my_number.append(calc_check_digit(my_number))
    return my_number


def verify_string(my_number_str):
    my_number = list(map(int, my_number_str))
    return verify_number(my_number)
