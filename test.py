#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import mynumber


class TestMyNumber(unittest.TestCase):

    test_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 0]

    def setUp(self):
        pass

    def test_check(self):
        print("Check digit calculation check")
        for n in range(0, 10):
            self.test_number[11] = n
            if not n == 8:
                print("Testing check digit: {0} / False".format(n))
                self.assertEqual(mynumber.verify_number(
                    self.test_number), False)
            else:
                print("Testing check digit: {0} / True".format(n))
                self.assertEqual(mynumber.verify_number(
                    self.test_number), True)


if __name__ == '__main__':
    unittest.main()
