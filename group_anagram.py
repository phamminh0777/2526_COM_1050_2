from collections import defaultdict
class Solution:
    def group_anagram(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())
sol = Solution()
strs = input().split()
print(sol.group_anagram(strs))


