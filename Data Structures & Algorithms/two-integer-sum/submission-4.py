class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, e in enumerate(nums):
            diff = target - e
            if diff in prev:
                return [prev[diff], i] 
            prev[e] = i