class Solution:
    def product(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        a = 1
        for i in range(len(nums)):
            res[i] = a
            a *= nums[i]
        re = [1] * len(nums)
        b = 1
        for i in range(len(nums) - 1, -1, -1):
            re[i] = b 
            b *= nums[i]
        for i in range(len(nums)):
            nums[i] = res[i] * re[i]
        return nums
sol = Solution()
nums = list(map(int, input().split()))
print(sol.product(nums))