import unittest

from contains_duplicate.solution import Solution


class TestContainsDuplicate(unittest.TestCase):

    def test_contains_duplicate(self):
        solution = Solution()

        nums = [1, 2, 3, 4]
        self.assertFalse(solution.containsDuplicate(nums))

        nums = [1, 2, 3, 4]
        self.assertFalse(solution.containsDuplicate(nums))
