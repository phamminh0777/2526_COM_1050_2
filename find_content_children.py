class Solution:
    def find_children(self, g: list[int], s: list[int]) -> int:
        l, r = 0, 0
        g.sort()
        s.sort()
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l += 1
            r += 1
        return l
sol = Solution()
g = list(map(int, input().split()))
s = list(map(int, input().split()))
print(sol.find_children(g, s))