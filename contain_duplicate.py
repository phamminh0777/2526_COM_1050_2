class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        num = set()
        for i in nums:
            if i in num:
                return True
            num.add(i)
        return False
sol = Solution()
nums = list(map(int, input().split()))
print(sol.has_duplicate(nums))