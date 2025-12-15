class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dicts = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dicts:
                return [dicts[a], i]
            dicts[nums[i]] = i
sol = Solution()
nums = list(map(int, input().split()))
target = int(input())
<<<<<<< HEAD
print(sol.two_sum(nums, target))
=======
print(sol.two_sum(nums, target))
>>>>>>> 5e63635f75c93c902678470e0f27cab11e456aa9
