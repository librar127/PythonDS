class Solution:
    def removeDuplicates(self, nums):
        
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                nums.pop(index+1)
            else:
                index += 1
        return len(nums)
    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums)) 