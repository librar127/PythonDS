class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_consecutive_ones = 0
        low = high = 0
        zero = 0
        k = 1
        
        while high < len(nums):
            
            if nums[high] == 0:
                zero += 1
            
            while zero > k:
                if nums[low] == 0:                    
                    zero -= 1
                low += 1
                
            max_consecutive_ones = max(max_consecutive_ones, high-low + 1)
            high += 1
            
        return max_consecutive_ones
    
    def findMaxConsecutiveOnes_2(self, nums):
        # previous and current length of consecutive 1 
        pre, curr, maxlen = -1, 0, 0
        for n in nums:
            if n == 0:
                pre, curr = curr, 0
            else:
                curr += 1
            maxlen = max(maxlen, pre + 1 + curr )
        
        return maxlen

s = Solution()
nums = [1,0,1,1,0]
print(s.findMaxConsecutiveOnes(nums))