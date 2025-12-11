class Solution:
    def remove(self, nums: list[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l
sol = Solution()
val = int(input())
nums = list(map(int, input().split()))
print(sol.remove(nums, val))