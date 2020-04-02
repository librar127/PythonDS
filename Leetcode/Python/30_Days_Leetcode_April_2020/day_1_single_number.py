class Solution:
    def singleNumber(self, nums):
        
        result = 0
        for each in nums:
            result ^= each
            
        return result
        