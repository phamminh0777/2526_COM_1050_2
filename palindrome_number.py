class Solution:
    def palindrome_number(self, x: int) -> bool:
        res = ""
        for i in str(x):
            res += i
        return res == res[::-1]
x = int(input())
sol = Solution()
print(sol.palindrome_number(x))