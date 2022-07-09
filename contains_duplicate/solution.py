class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        vals = {}
        for num in nums:
            if num in vals:
                return True
            else:
                vals[num] = True
        return False


solution = Solution()

values = range(1, 99999)

print(solution.containsDuplicate(values))
