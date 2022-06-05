class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            i = left + int(right - left / 2)
            if nums[i] == target:
                return i
            if nums[i] < target:
                left = i + 1
                continue
            if nums[i] > target:
                right = i - 1
                continue
        return -1
