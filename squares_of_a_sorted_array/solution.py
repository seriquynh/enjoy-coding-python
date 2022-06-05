class Solution:
    def sortedSquares(self, nums: list) -> list:
        nums.sort()

        results = []

        for num in nums:
            results.append(num**2)

        results.sort()

        return results
