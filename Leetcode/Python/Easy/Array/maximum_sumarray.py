class Solution:
    ### Dynamic Programming
    def maxSubArray(self, nums):
        if len(nums) <= 0:
            return 0
        
        sum = nums[0]
        index = 0
        max_sum = sum
        for index in range(1, len(nums)):            
            if sum + nums[index] > nums[index]:
                sum += nums[index]
            else:
                sum = nums[index]
                
            if sum > max_sum:
                max_sum = sum
            
        return max_sum
        
                
solution = Solution()
input_list = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(input_list))