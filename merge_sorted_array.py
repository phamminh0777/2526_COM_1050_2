class Solution:
    def merge(self, num1: list[int], m: int, num2: list[int], n: int) -> list[int]:
        l = m - 1
        r = n -1
        k = m + n -1
        while l >= 0 and r >= 0:
            if num1[l] < num2[r]:
                num1[k] = num2[r]
                r -= 1
            else:
                num1[k] = num1[l]
                l -= 1
            k -= 1
        while r >=0:
            num1[k] = num2[r]
            r -= 1
            k -= 1
        while l >= 0:
            num1[k] = num1[l]
            l -= 1
            k -= 1
        return num1
sol = Solution()
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
m = int(input())
n = int(input())
print(sol.merge(num1, m, num2, n))