from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for item in strs:
            key = "".join(sorted(item))
            output[key].append(item)

        return list(output.values())
        