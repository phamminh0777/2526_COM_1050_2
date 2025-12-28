class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        idx, d = 0, 1
        row = [''] * numRows
        for char in s:
            row[idx] += char
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        return "".join(row)
s = "PAYPALISHIRING"
numRows = 3
sol = Solution()
print(sol.convert(s, numRows))