class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output={}

        for item in strs:
            h_key = "".join(sorted(item))
            if h_key not in output:
                output[h_key] = []
            output[h_key].append(item)
        
        return list(output.values())
        