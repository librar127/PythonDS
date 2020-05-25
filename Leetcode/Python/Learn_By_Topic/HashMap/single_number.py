class Solution:
    def singleNumber(self, nums):
        
        # Solution 1
        hashset = set(nums)
        sum = 0
        for each in hashset:
            sum += each * 2

        for each in nums:
            sum -= each

        #return sum
    
        # Solution 2
        xor = 0        
        for each in nums:
            xor ^= each
        return xor