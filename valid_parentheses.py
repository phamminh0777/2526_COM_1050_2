class Solution:
    def valid_parentheses(self, s: str) -> bool:
        notation = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for i in s:
            if i not in notation:
                stack.append(i)
            else:
                if stack and stack[-1] == notation[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
sol = Solution()
s = input()
print(sol.valid_parentheses(s))

