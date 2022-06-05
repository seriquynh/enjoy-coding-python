import unittest

from squares_of_a_sorted_array.solution import Solution


class TestSquaresOfASortedArray(unittest.TestCase):

    def test_squares_of_a_sorted_array(self):
        solution = Solution()

        expected = [0, 1, 9, 16, 100]
        actual = solution.sortedSquares([-4,-1,0,3,10])

        self.assertEqual(expected, actual)
