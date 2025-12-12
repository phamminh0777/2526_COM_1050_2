class Solution:
    def is_valid(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0] * 26
        for i in range(len(s)):
            table[ord(s[i]) - ord("a")] += 1
            table[ord(t[i]) - ord("a")] -= 1
        for j in table:
            if j != 0:
                return False
        return True
sol = Solution()
s = input()
t = input()
print(sol.is_valid(s, t))