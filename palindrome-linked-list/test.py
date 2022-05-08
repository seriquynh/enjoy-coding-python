#!/usr/bin/env python

import yaml
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True

        values = []

        current = head

        while current is not None:
            values.append(current.val)

            current = current.next

        return self.list_is_palindrome(values)

    @staticmethod
    def list_is_palindrome(values: list) -> bool:
        left = 0
        size = len(values)
        right = size - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left = left + 1
            right = right - 1

        return True


class TestPalindromeLinkedList(unittest.TestCase):

    def test_palindrome_linked_list(self):
        with open("../enjoy-coding/palindrome-linked-list/test-cases.yaml", "r") as stream:
            try:
                test_cases = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return

        solution = Solution()

        for test_case in test_cases['test_cases']:
            input_value = test_case[0]
            expected = test_case[1]
            actual = solution.list_is_palindrome(input_value)
            self.assertEqual(expected, actual)
        pass


if __name__ == '__main__':
    unittest.main()
