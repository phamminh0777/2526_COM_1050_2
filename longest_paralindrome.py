class Solution:
    def longest(self, s: str) -> int:
        count = {}
        long = 0
        a = False
        for i in s:
            count[i] = 1 + count.get(i, 0)
        for value in count.values():
            long += (value // 2) * 2
            if value % 2 != 0:
                a = True
        if a:
            return long + 1
        return long
sol = Solution()
s = input()
print(sol.longest(s))
