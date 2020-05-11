class Solution:
    def findNumbers(self, nums):
        count = 0
        
        for each in nums: 
            digit_count = 0
            while each > 0:
                
                each = each // 10
                digit_count += 1
                    
            if digit_count % 2 == 0:
                count += 1
                
        return count
    
s  = Solution()
nums = [12,345,2,6,7896]
print(s.findNumbers(nums))