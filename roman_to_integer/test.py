#!/usr/bin/env python

import unittest
import yaml


from roman_to_integer.solution import Solution


class TestRomanToInteger(unittest.TestCase):

    def test_roman_to_integer(self):
        with open("../enjoy-coding/roman-to-integer/test-cases.yaml", "r") as stream:
            try:
                test_cases = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return

        solution = Solution()

        for test_case in test_cases['test_cases']:
            input_value = test_case[0]
            expected = test_case[1]
            actual = solution.romanToInt(input_value)
            self.assertEqual(expected, actual)
