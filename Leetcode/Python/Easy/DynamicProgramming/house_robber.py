class Solution:
    # Tn = O(N) Sn = O(N)
    def rob_1(self, nums):
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        sol_list = []
        sol_list.append(nums[0])
        sol_list.append(max(nums[0], nums[1]))
        
        for index in range(2, len(nums)):
            
            curr_selected = nums[index] + sol_list[index-2]            
            curr_not_selected = sol_list[index-1]
            
            sol_list.append(max(curr_selected, curr_not_selected))
            
        return sol_list[len(nums)-1]
    
    # Tn = O(N) Sn = O(1)        
    def rob(self, nums)t:
        
        if not nums:
            return 0   
        
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1]) 
        
        prev_2 = nums[0]
        prev_1 = max(nums[0], nums[1])   
        
        for index in range(2, len(nums)):
            current = nums[index] + prev_2
            prev_2 = prev_1
            prev_1 = max(prev_2, current)
            
        return prev_1