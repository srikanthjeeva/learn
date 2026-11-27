class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_counter={}

        for num in nums:
            num_counter[num] = num_counter.get(num, 0) + 1

        return sorted(num_counter, key=num_counter.get, reverse=True)[:k]
        