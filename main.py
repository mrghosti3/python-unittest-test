#!/bin/python3
import unittest

class NegativeNumException(Exception):
    """ Negative number exception.
    """
    def __init__(self, neg_nums):
        super().__init__(f"NegativeNumException: Negative numbers in equation: {neg_nums}.")
        self.negative_nums = neg_nums

def add(numbers: str) -> int:
    """Add method to calculate simple summation.

    Args:
        numbers (str): text of numbers to add

    Returns:
        int: summed result
    """

    delimitter = ','
    n_str = numbers

    if numbers.startswith('//'):
        delimitter, n_str = numbers.split('\n', 1)
        delimitter = delimitter[2:]

    n_list = n_str.split(delimitter)
    summation = 0
    negative_nums = list()

    for n_set in n_list:
        if n_set == '':
            return 0
        elif len(n_set) == 1 and n_set == '\n':
            return 0
        else:
            pass

        for snum in n_set.split('\n'):
            num = int(snum)
            if num < 0:
                negative_nums.append(num)
            elif len(negative_nums) > 0:
                continue
            elif num < 1001:
                summation += int(snum)

    if len(negative_nums) > 0:
        raise NegativeNumException(negative_nums)

    return summation


class TestAddMethod(unittest.TestCase):
    """
    add method unit test class
    """

    def test_empty_string(self):
        """
        Test 1:
        Input = '', result = 0
        """
        self.assertEqual(add(''), 0)

    def test_two_plus_four_string(self):
        """
        Test 2:
        Input = '2,4', expected result = 6
        """
        self.assertEqual(add('2,4'), 6)

    def test_one_number_string(self):
        """
        Test 3:
        Input = '1', result = 1
        """
        self.assertEqual(add('1'), 1)

    def test_semicolon_delim_string_test(self):
        """
        Test 4:
        Input = '//;\n2;4', delimitter = ';' and result = 6
        """
        self.assertEqual(add('//;\n2;4'), 6)

    def test_negative_num(self):
        """
        Test 5:
        Input = '2,-4,-3', result = Exception with every negative number
        """
        with self.assertRaises(NegativeNumException):
            add('2,-4,-3')

    def test_too_large_num(self):
        """
        Test 6
        Input = '2,4,1001' , result = 6
        """
        self.assertEqual(add('2,4,1001'), 6)

    def test_longer_delim_string(self):
        """
        Test 7
        Input = '//***\\n2***4' , delimitter = '***' AND result = 6
        """
        self.assertEqual(add('//***\n2***4'), 6)

if __name__ == "__main__":
    unittest.main()
