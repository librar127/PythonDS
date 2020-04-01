class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums) <= 0:
            return 0
        
        new_index = 0
        index = 1
        while index < len(nums):
            while nums[new_index] == nums[index]:
                if index >= len(nums)-1:
                    return new_index+1
                index += 1
                
            new_index += 1
            nums[new_index] = nums[index]           
            
                
        return new_index+1
    
s = Solution()
print(s.removeDuplicates([]))