
import os
import unittest
import sys


def addition(x, y):
    """
    Adds two numbers; this is the method that's being tested.

    :param x: number 1
    :param y: number 2
    :returns: sum of two numbers
    """
    return x + y


def subtract(x,y):

    return x-y

class AdditionTesting(unittest.TestCase):
    """Unit test that tests add(x, y) defined above using the test data from the test data class."""

    def test1(self):
        self.assertEqual(addition(6,4), 10)
    def test2(self):
        self.assertEqual(subtract(3,3), 0)

if __name__ == '__main__':
    unittest.main()
