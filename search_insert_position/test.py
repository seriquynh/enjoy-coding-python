import unittest

from search_insert_position.solution import Solution


class TestSearchInsertPosition(unittest.TestCase):

    def test_search_insert_position(self):
        solution = Solution()

        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        actual = solution.searchInsert(nums, target)

        self.assertEqual(expected, actual)

        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        actual = solution.searchInsert(nums, target)

        self.assertEqual(expected, actual)
