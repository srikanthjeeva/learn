class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh = {}
        for i, n in enumerate(nums):
            if n in hsh:
                return True
            hsh[n] = i
        return False

        