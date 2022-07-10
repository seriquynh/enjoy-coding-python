import unittest

import helpers
from maximum_subarray.solution import Solution


class TestMaximumSubarray(unittest.TestCase):

    def test_maxinum_subarray(self):
        solution = Solution()

        for test_case in helpers.get_test_cases('maximum-subarray'):
            nums = test_case['input']['nums']
            target = test_case['input']['target']
            expected = test_case['output']
            actual = solution.search(nums, target)
            self.assertEqual(expected, actual)
