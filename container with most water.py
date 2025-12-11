class Solution:
    def contain(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        area = 0
        while l < r:
            width = r - l
            h = min(nums[l], nums[r])
            s = width * h
            area = max(area, s)
            if nums[l] <= nums[r]:
                l += 1
            else:
                r -= 1
        return area
sol = Solution()
nums = list(map(int, input().split()))
print(sol.contain(nums))