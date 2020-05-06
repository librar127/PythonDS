class Solution:
    def maxSubArray(self, nums):
        
        if len(nums) <= 1:
            return nums[0]
        
        sum_so_far = 0
        max_sum = -999 #minimum num supported
        for each in nums:
            if sum_so_far + each > each:
                sum_so_far += each
            else:
                sum_so_far = each
                
            if sum_so_far > max_sum:
                max_sum = sum_so_far
                
        return max_sum
        