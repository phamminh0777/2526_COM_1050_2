class Solution:
    def topk(self, nums: list[int], k: int) -> list[int]:
        fre = [[] for i in range(len(nums))]
        count = {}
        for s in nums:
            count[s] = 1 + count.get(s, 0)
        for key, value in count.items():
            fre[value].append(key)
        res = []
        for i in range(len(nums) - 1, 0, -1):
            for j in fre[i]:
                res.append(j)
                if len(res) == k:
                    return res
nums = list(map(int, input().split()))
k = int(input())
sol = Solution()
print(sol.topk(nums, k))