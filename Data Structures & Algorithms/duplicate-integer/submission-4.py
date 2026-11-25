class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given nums[1,2,3,3]
        # find duplicate, return true if duplicate or false

        # lets define a set(). and iternate and check if num in set

        allnums = set()

        for num in nums:
            if num in allnums:
                return True
            
            allnums.add(num)
        return False