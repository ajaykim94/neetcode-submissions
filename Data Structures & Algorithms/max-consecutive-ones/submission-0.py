class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for i in nums:
            count +=1 if i else -count
            res = max(res, count)
        return res