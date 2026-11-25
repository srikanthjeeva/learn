class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given nums, target
        # find if 2 numbers add up to each other
        # target-num=another num.
        # push to hashmap and find if num and another num is there 
        # return the indices as array

        hsh = {}
        for i, num in enumerate(nums):
            compliment=target-num
            if compliment in hsh:
                return [hsh[compliment], i]

            hsh[num] = i
