class Solution:
    def remove_duplicate(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
sol = Solution()
nums = list(map(int, input().split()))

print(sol.remove_duplicate(nums))