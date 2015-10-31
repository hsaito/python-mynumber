#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random


def verify_number(my_number):
    """Verify 'My Number' for its integrity"""

    if len(my_number) != 12:
        raise TypeError("Malformed My Number -- Must be 12 numbers")

    check_digit = calc_check_digit(my_number[:11])
    if my_number[11] == check_digit:
        return True
    else:
        return False


def calc_check_digit(my_number):
    """Calculates check digits"""
    my_number_sum = 0

    if len(my_number) != 11:
        raise TypeError("Malformed My Number Segment -- Must be 11 numbers")

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


def gen_random_number():
    """For testing, generate random 'My Number'"""
    my_number = []
    for n in range(11):
        my_number.append(random.randint(0, 9))
    my_number.append(calc_check_digit(my_number))
    return my_number


def verify_string(my_number_str):
    """Verify 'My Number' string"""
    my_number = list(map(int, my_number_str))
    return verify_number(my_number)


def check_list(nlist):
    """Check to see if the list only contains [0-9]"""
    for n in range(len(nlist)):
        if not 0 <= nlist[n] <= 9:
            return False
    return True
