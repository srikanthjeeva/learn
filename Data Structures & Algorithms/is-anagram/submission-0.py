class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hshs, hshy = {}, {}

        for i in range(len(s)):
            hshs[s[i]] = 1 + hshs.get(s[i], 0)
            hshy[t[i]] = 1 + hshy.get(t[i], 0)

        return hshs == hshy
        