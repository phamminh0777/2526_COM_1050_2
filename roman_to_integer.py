class Solution:
    def roman_integer(self, s: str) -> int:
        a = 0
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        for i, j in zip(s, s[1:]):
            if roman[i] < roman[j]:
                a -= roman[i]
            else:
                a += roman[i]
        return a + roman[s[-1]]
s = input()
sol = Solution()
print(sol.roman_integer(s))
