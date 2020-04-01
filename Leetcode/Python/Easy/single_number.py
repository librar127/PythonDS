class Solution:
    def singleNumber(self, nums):
        result = 0
        for each in nums:
            result ^= each
            
        return result
    
s = Solution()
print(s.singleNumber([2,2,1]))
        