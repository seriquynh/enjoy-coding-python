import unittest

import helpers
from roman_to_integer.solution import Solution


class TestRomanToInteger(unittest.TestCase):

    def test_roman_to_integer(self):
        solution = Solution()

        for test_case in helpers.get_test_cases('roman-to-integer'):
            input_value = test_case['input']
            expected = test_case['output']
            actual = solution.romanToInt(input_value)
            self.assertEqual(expected, actual)
