import unittest

import helpers
from binary_search.solution import Solution


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        solution = Solution()

        for test_case in helpers.get_test_cases('binary-search'):
            nums = test_case['input']['nums']
            target = test_case['input']['target']
            expected = test_case['output']
            actual = solution.search(nums, target)
            self.assertEqual(expected, actual)
