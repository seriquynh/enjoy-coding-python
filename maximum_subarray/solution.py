class Solution:
    def maxSubArray(self, nums: list) -> int:
        best_sum = max(nums)
        best_sum = max(best_sum, sum(nums))
        current_sum = 0

        for num in nums:
            current_sum = current_sum + num
            if current_sum < 0:
                current_sum = 0
                continue
            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum
