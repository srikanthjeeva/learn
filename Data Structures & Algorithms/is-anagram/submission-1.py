class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram means same characters with number of times
        # lets store both in hashmap
        # lets run 1 loop so that it would be o(n), space is o(1)
        if len(s) != len (t):
            return False 
        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1

        return sCount==tCount
        