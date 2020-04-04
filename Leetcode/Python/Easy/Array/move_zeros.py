class Solution:
    
    ### 1. Solution with extra-space
    def moveZeroes_extra_space(self, nums): 
        new_list = []
        
        zero_count = 0
        for each_item in nums:
            if each_item == 0:
                zero_count += 1
            else:
                new_list.append(each_item)
        
        new_list.extend([0]*zero_count)
        return new_list
    
    ### 2. In-Place Solution    
    def moveZeroes(self, nums):
        
        """
        Do not return anything, modify nums in-place instead.
        """
        for index, each_item in enumerate(nums):
            if each_item == 0:
                nums.remove(nums[index])
                nums.append(each_item)
                            
        return nums               

solution = Solution()
num_list = [0,0,1]
print(solution.moveZeroes_extra_space(num_list))
print(solution.moveZeroes(num_list))