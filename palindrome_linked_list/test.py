import unittest

import helpers
from palindrome_linked_list.solution import Solution


class TestPalindromeLinkedList(unittest.TestCase):

    def test_palindrome_linked_list(self):
        solution = Solution()

        for test_case in helpers.get_test_cases('palindrome-linked-list'):
            input_value = test_case['input']
            expected = test_case['output']
            actual = solution.list_is_palindrome(input_value)
            self.assertEqual(expected, actual)
