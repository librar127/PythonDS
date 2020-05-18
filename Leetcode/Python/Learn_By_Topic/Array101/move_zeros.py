class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = 0
        
        for index, each in enumerate(nums):
            if each != 0:
                nums[index], nums[zero] = nums[zero], nums[index]
                zero += 1
            else:
                pass
            
        return nums
    
s =Solution()
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))