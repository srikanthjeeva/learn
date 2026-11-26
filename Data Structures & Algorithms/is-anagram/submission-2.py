class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        s_hsh,t_hsh = {}, {}

        for index in range(len(s)):
            s_hsh[s[index]] = s_hsh.get(s[index], 0) + 1
            t_hsh[t[index]] = t_hsh.get(t[index], 0) + 1
        
        return s_hsh == t_hsh
