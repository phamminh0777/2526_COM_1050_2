class Solution:
    def majority(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key in count:
            if count[key] > len(nums) // 2:
                return key
sol = Solution()
nums = list(map(int, input().split()))
print(sol.majority(nums))
