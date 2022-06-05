import unittest

import helpers
from palindrome_linked_list.solution import Solution


class TestPalindromeLinkedList(unittest.TestCase):

    def test_palindrome_linked_list(self):
        solution = Solution()

        for test_case in helpers.get_test_cases('palindrome-linked-list'):
            input_value = test_case[0]
            expected = test_case[1]
            actual = solution.list_is_palindrome(input_value)
            self.assertEqual(expected, actual)
