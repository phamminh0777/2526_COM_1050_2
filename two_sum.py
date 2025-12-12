class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dicts = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dicts:
                return [dicts[a], i]
            dicts[nums[i]] = i
sol = Solution()
nums = [1, 2, 3]
target = 2
print(sol.two_sum(nums, target))