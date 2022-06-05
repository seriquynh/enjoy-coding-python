import yaml
import unittest

from palindrome_linked_list.solution import Solution


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
