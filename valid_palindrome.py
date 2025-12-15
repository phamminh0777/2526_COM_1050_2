class Solution:
    def palindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
        return res == res[::-1]
sol = Solution()
s = input()
print(sol.palindrome(s))