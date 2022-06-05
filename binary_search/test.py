import yaml
import unittest

from binary_search.solution import Solution


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        with open("../enjoy-coding/binary-search/test-cases.yaml", "r") as stream:
            try:
                test_cases = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return

        solution = Solution()

        for test_case in test_cases['test_cases']:
            nums = test_case['input']['nums']
            target = test_case['input']['target']
            expected = test_case['output']
            actual = solution.search(nums, target)
            self.assertEqual(expected, actual)
